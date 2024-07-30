#!/usr/bin/python3

"""
moduel
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello():
    """ displays Hello World """

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ displays HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ displays c and the text """
    return "C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """ displays python and the text """
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ displays n if is a number """
    return str(n) + " is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
