#!/usr/bin/python3
"""
iam here
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    return html
    """
    return "HELLO HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
