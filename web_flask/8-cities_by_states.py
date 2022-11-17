#!/usr/bin/python3
"""
This module starts a Flask web application
"""
from flask import Flask, render_template
from models import storage, state, city

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def states_list():
    return render_template(
        "8-cities_by_states.html",
        states=storage.all(state.State),
        cities=storage.all(city.City)
        )


@app.teardown_appcontext
def teardown(something):
    """Call close"""
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
