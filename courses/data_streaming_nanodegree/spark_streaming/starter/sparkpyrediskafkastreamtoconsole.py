from pyspark.sql import SparkSession
from pyspark.sql.functions import (base64, col, expr, from_json, split,
                                   to_json, unbase64)
from pyspark.sql.types import (ArrayType, BooleanType, DateType, FloatType,
                               StringType, StructField, StructType)

# TO-DO: create a StructType for the Kafka redis-server topic which has all changes made to Redis
schema_redis_kafka = StructType(
    [
        StructField("key", StringType()),
        StructField("existType", StringType()),
        StructField("Ch", BooleanType()),
        StructField("Incr", BooleanType()),
        StructField(
            "zSetEntries",
            ArrayType(
                StructType(
                    [
                        StructType(
                            [
                                StructField("element", StringType()),
                                StructField("score", StringType()),
                            ]
                        )
                    ]
                )
            ),
        ),
    ]
)
# TO-DO: create a StructType for the Customer JSON that comes from Redis- before Spark 3.0.0, schema inference is not automatic
schema_json_customer = StructType(
    [
        StructField("customerName", StringType()),
        StructField("email", StringType()),
        StructField("phone", StringType()),
        StructField("birthDay", StringType())
    ]
)
# TO-DO: create a StructType for the Kafka stedi-events topic which has the Customer Risk JSON that comes from Redis- before Spark 3.0.0, schema inference is not automatic
schema_events_kafka = StructType(
    [
        StructField("customer", StringType()),
        StructField("score", FloatType()),
        StructField("riskDate", DateType())
    ]
)
# TO-DO: create a spark application object
spark = SparkSession.builder.appName("rktc-cust-record").getOrCreate()

# TO-DO: set the spark log level to WARN
spark.sparkContext.setLogLevel('WARN')

# TO-DO: using the spark application object, read a streaming dataframe from the Kafka topic redis-server as the source
# Be sure to specify the option that reads all the events from the topic including those that were published before you started the spark stream

DFRedisServerRaw = spark \
    .readStream \
        .format("kafka") \
            .option("kafka.bootstrap.servers","localhost:9092") \
                .option("subscribe","redis-server"). \
                    option("startgOffsets","earliest") \
                        .load()

# TO-DO: cast the value column in the streaming dataframe as a STRING
DFRedisServer = DFRedisServerRaw \
    .selectExpr("cast(value as string) value")
# TO-DO:; parse the single column "value" with a json object in it, like this:
# +------------+
# | value      |
# +------------+
# |{"key":"Q3..|
# +------------+
#
# with this JSON format: {"key":"Q3VzdG9tZXI=",
# "existType":"NONE",
# "Ch":false,
# "Incr":false,
# "zSetEntries":[{
# "element":"eyJjdXN0b21lck5hbWUiOiJTYW0gVGVzdCIsImVtYWlsIjoic2FtLnRlc3RAdGVzdC5jb20iLCJwaG9uZSI6IjgwMTU1NTEyMTIiLCJiaXJ0aERheSI6IjIwMDEtMDEtMDMifQ==",
# "Score":0.0
# }],
# "zsetEntries":[{
# "element":"eyJjdXN0b21lck5hbWUiOiJTYW0gVGVzdCIsImVtYWlsIjoic2FtLnRlc3RAdGVzdC5jb20iLCJwaG9uZSI6IjgwMTU1NTEyMTIiLCJiaXJ0aERheSI6IjIwMDEtMDEtMDMifQ==",
# "score":0.0
# }]
# }
#
# (Note: The Redis Source for Kafka has redundant fields zSetEntries and zsetentries, only one should be parsed)
#
# and create separated fields like this:
# +------------+-----+-----------+------------+---------+-----+-----+-----------------+
# |         key|value|expiredType|expiredValue|existType|   ch| incr|      zSetEntries|
# +------------+-----+-----------+------------+---------+-----+-----+-----------------+
# |U29ydGVkU2V0| null|       null|        null|     NONE|false|false|[[dGVzdDI=, 0.0]]|
# +------------+-----+-----------+------------+---------+-----+-----+-----------------+
#
# storing them in a temporary view called RedisSortedSet
DFRedisServer \
    .withColumn("value", from_json("value", schema_redis_kafka)) \
        .select(
            col('value.existType'),
             col('value.Ch'),
              col('value.Incr'),
               col('value.zSetEntries')) \
            .createOrReplaceTempView('RedisSortedSet')
# TO-DO: execute a sql statement against a temporary view, which statement takes the element field from the 0th element in the array of structs and create a column called encodedCustomer
# the reason we do it this way is that the syntax available select against a view is different than a dataframe, and it makes it easy to select the nth element of an array in a sql column
DFzSetEntries = spark.sql(
    "select key, zSetEntries[0].element as encodedCustomer from RedisSortedSet"
    )
# TO-DO: take the encodedCustomer column which is base64 encoded at first like this:
# +--------------------+
# |            customer|
# +--------------------+
# |[7B 22 73 74 61 7...|
# +--------------------+
DFzSetEntries=DFzSetEntries \
    .withColumn(
        "customer", unbase64(DFzSetEntries.encodedCustomer
        ) \
            .cast("string"))

# TO-DO: parse the JSON in the Customer record and store in a temporary view called CustomerRecords
DFzSetEntries \
    .withColumn(
        "customer", from_json("customer", schema_json_customer
        )) \
            .select(
                col("customer.*")
                ) \
                .createOrReplaceTempView(
                    "CustomerRecords"
                    )
# and convert it to clear json like this:
# +--------------------+
# |            customer|
# +--------------------+
# |{"customerName":"...|
# +--------------------+
#
# with this JSON format: {"customerName":"Sam Test","email":"sam.test@test.com","phone":"8015551212","birthDay":"2001-01-03"}

# TO-DO: parse the JSON in the Customer record and store in a temporary view called CustomerRecords

# TO-DO: JSON parsing will set non-existent fields to null, so let's select just the fields we want, where they are not null as a new dataframe called emailAndBirthDayStreamingDF
emailAndBirthDayStreamingDF = spark.sql(
    """select email, birthday from CustomerRecords where email is not null and birthDay is not null"""
    )

# TO-DO: Split the birth year as a separate field from the birthday
emailAndBirthDayStreamingDF = emailAndBirthDayStreamingDF \
    .withColumn(
        'birthYear', split(emailAndBirthDayStreamingDF.birthDay,"-"
        ) \
            .getItem(0))

# TO-DO: Select only the birth year and email fields as a new streaming data frame called emailAndBirthYearStreamingDF
emailAndBirthYearStreamingDF = emailAndBirthDayStreamingDF \
    .select(
        col('email'),
        col('birthYear')
        )

# TO-DO: sink the emailAndBirthYearStreamingDF dataframe to the console in append mode
emailAndBirthYearStreamingDF.writeStream.outputMode("append").format("console").start().awaitTermination()
# The output should look like this:
# +--------------------+-----
# | email         |birthYear|
# +--------------------+-----
# |Gail.Spencer@test...|1963|
# |Craig.Lincoln@tes...|1962|
# |  Edward.Wu@test.com|1961|
# |Santosh.Phillips@...|1960|
# |Sarah.Lincoln@tes...|1959|
# |Sean.Howard@test.com|1958|
# |Sarah.Clark@test.com|1957|
# +--------------------+-----

# Run the python script by running the command from the terminal:
# /home/workspace/submit-redis-kafka-streaming.sh
# Verify the data looks correct
