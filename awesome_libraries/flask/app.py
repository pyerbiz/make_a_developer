from flask import Flask, request

app = Flask(__name__)


@app.route("/api/foo/", methods=["GET"])
def foo():
    bar = request.args.to_dict()
    print(bar)
    return "success", 200


if __name__ == "__main__":
    app.run(debug=True)
