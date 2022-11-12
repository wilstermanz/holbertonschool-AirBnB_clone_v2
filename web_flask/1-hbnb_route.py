#!/usr/bin/python3
"""
This module starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    return 'Hello HBNB!'


@app.route("/hbnb")
def hbnb():
    return 'HBNB'


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
