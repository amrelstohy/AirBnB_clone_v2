#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def lets_add_logic(id):
    """
    iam here
    """
    states = storage.all("State")
    full_name = "State." + id
    if full_name in states:
        obj = states['{}'.format(full_name)]
        cities = sorted(obj.cities, key=lambda x: x.name)
        return render_template('9-states.html', state=obj.name, cities=cities)
    else:
        return render_template('9-states.html')


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
