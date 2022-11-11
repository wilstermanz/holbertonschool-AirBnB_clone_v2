#!/usr/bin/python3
"""Task 2: Script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape


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


@app.route("/c/<string:text>")
def c_text(text):
    """Document"""
    text = text.replace("_", " ")
    return f'C {text}'


if __name__ == "__main__":
    """Document"""
    app.run(host="0.0.0.0", port="5000")
