#!/usr/bin/python3
"""
getting database_data
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def get_states():
    """
    retrieving html page
    """
    states = sorted(storage.all().values(),
                    key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tearingdown_db_session(exception=None):
    """
    tear down
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
