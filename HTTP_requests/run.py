from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/get", methods=["GET"])
def get_request():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    print(response)
    if response:
        return response.json(), 200
    return jsonify({"message": "Error while fetching"}), 404

@app.route("/getmyposts", methods=["GET"])
def get_posts_request():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/109")
    print(response)
    if response:
        return response.json(), 200
    return jsonify({"message": "Error while fetching"}), 404

@app.route("/posthttp", methods=["GET"])
def post_request():
    response = requests.post("https://jsonplaceholder.typicode.com/posts", params={"userId": 2, "id": 250, "title": "New title", "body": "New body"})
    if response:
        return jsonify({"message": "Post successful"}), 200
    return jsonify({"message": "Post failed"}), 400

if __name__ == "__main__":
    app.run(port="8080", debug=True)