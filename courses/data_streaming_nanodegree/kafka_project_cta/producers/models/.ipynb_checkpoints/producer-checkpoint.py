"""Producer base-class providing common utilites and functionality"""
import logging
import time

from confluent_kafka import avro  # avro serialization
from confluent_kafka.admin import AdminClient, NewTopic  # topic creation
from confluent_kafka.avro import AvroProducer  # produce a stream with avro schema

logger = logging.getLogger(__name__)

ZOOKEEPER_URL = "localhost:2181"
SCHEMA_REGISTRY_URL = "http://localhost:8081"
BROKER_URL = "PLAINTEXT://localhost:9092"


class Producer:
    """Defines and provides common functionality amongst Producers"""

    # Tracks existing topics across all Producer instances
    existing_topics = set()

    def __init__(
        self,
        topic_name,
        key_schema,
        value_schema=None,
        num_partitions=1,
        num_replicas=1,
    ):
        """Initializes a Producer object with basic settings"""
        self.topic_name = topic_name
        self.key_schema = key_schema
        self.value_schema = value_schema
        self.num_partitions = num_partitions
        self.num_replicas = num_replicas

        #
        #
        # TODO: Configure the broker properties below. Make sure to reference the project README
        # and use the Host URL for Kafka and Schema Registry!
        #
        #
        self.broker_properties = {
            "schema.registry.url": SCHEMA_REGISTRY_URL,
            "bootstrap.servers": BROKER_URL,
        }

        # If the topic does not already exist, try to create it
        if self.topic_name not in Producer.existing_topics:
            self.create_topic()
            Producer.existing_topics.add(self.topic_name)

        # TODO: Configure the AvroProducer
        self.producer = AvroProducer(
            {
                "bootstrap.servers": BROKER_URL,
                "schema.registry.url": SCHEMA_REGISTRY_URL,
            },
            default_key_schema=key_schema,
            default_value_schema=value_schema,
        )

    def create_topic(self):
        """Creates the producer topic if it does not already exist"""
        #
        #
        # TODO: Write code that creates the topic for this producer if it does not already exist on
        # the Kafka Broker.
        #
        #
        client = AdminClient({"bootstrap.servers": BROKER_URL})
        topic_list = client.list_topics()

        topics_properties = client.create_topics(
            [
                NewTopic(
                    topic=self.topic_name,
                    num_partitions=self.num_partitions,
                    replication_factor=self.num_replicas,
                    config={
                        "compression.type": "lz4",
                        "delete.retention.ms": "80",
                        "cleanup.policy": "delete",
                    },
                )
            ]
        )

        # NTH:import KafkaError, use its properties to be more specific
        for topic, properties in topics_properties.items():
            try:
                properties.result()
                logger.info(f"Created {topic} Topic successfully")
            except Exception as ex:
                logger.info(f"Topic {topic} not created because \n {ex}")
                continue

    def time_millis(self):
        return int(round(time.time() * 1000))

    def close(self):
        """Prepares the producer for exit by cleaning up the producer"""
        #
        #
        # TODO: Write cleanup code for the Producer here
        #
        #
        # logger.info("producer close incomplete - skipping")
        if self.producer is not None:
            self.producer.flush()

    def time_millis(self):
        """Use this function to get the key for Kafka Events"""
        return int(round(time.time() * 1000))
