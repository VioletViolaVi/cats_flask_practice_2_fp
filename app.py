from flask import Flask, request, jsonify
from flask_cors import CORS

from controllers import cats

app = Flask(__name__)
CORS(app)


@app.route("/")
def welcome():
    return "Welcome to flask"


@app.route("/cats", methods=["GET", "POST"])
def cat():
    # if request.method == "GET":
    #     return jsonify({"cats": ["Muffy", "Luffy"]}), 200
    # elif request.method == "POST":
    #     return "We have 'POST' some cats", 201
    fns = {
        "GET": cats.index,
        "POST": cats.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code


if __name__ == "__main__":
    app.run(debug=True)
