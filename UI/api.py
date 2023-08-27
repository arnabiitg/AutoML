from flask import Flask, render_template, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
from dataingestion import connect



@app.route("/api/endpoint",methods = ["GET"])
def apiresponse():
    return(jsonify(connect.makedata()))


if __name__ == "__main__":
    app.run(debug= True, port = 7000)