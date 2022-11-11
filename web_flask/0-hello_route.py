#!/usr/bin/python3
"""Task 0: Script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    """Document"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """Document"""
    app.run(host="0.0.0.0", port="5000")
