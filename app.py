from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/upload', methods=['GET'])
def upload():
    return jsonify({"message": "successful"})


@app.route('/download', methods=['GET'])
def download():
    return jsonify({"message": "downloading"})


@app.route('/')
def helloworld():
    return "hello world"
