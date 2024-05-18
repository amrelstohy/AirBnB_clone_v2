#!usr/bin/python3
"""
iam here
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_main():
    """
    main DIR
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """
    hbnb dir
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
