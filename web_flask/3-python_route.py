#!/usr/bin/python3
"""Task 3: Script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    """Document"""
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    """Document"""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """Document"""
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route("/python/<text>")
def python_text(text="is cool"):
    """Document"""
    text = text.replace("_", " ")
    return ("Python {}".format(text))


if __name__ == "__main__":
    """Document"""
    app.run(host="0.0.0.0", port="5000")
