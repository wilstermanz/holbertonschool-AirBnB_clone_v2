#!/usr/bin/python3
"""
This module starts a Flask web application
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    return 'Hello HBNB!'


@app.route("/hbnb")
def hbnb():
    return 'HBNB'


@app.route("/c/<text>")
def c_text(text):
    text = text.replace('_', ' ')
    return "C {}".format(escape(text))


@app.route("/python/<text>")
def python_text(text="is cool"):
    text = text.replace('_', ' ')
    return "Python {}".format(escape(text))


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
