from flask import Flask
from flaskext.mysql import MySQL
import os


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Python!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
