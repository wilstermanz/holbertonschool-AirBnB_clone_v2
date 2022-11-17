#!/usr/bin/python3
"""
This module starts a Flask web application
"""
from flask import Flask, render_template
from models import storage, state, city

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states/<id>")
def states_id(id):
    states = storage.all(state.State)
    return render_template("9-states.html", states=states, id=id)


@app.route("/states")
def states():
    states = storage.all(state.State)
    return render_template("9-states.html", states=states, id=None)


@app.teardown_appcontext
def teardown(something):
    """Call close"""
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
