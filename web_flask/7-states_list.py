#!/usr/bin/python3
"""
Start a flask web application
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states():
    """
    Fetch list of all states in storage
    """
    from models.state import State
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown(exc):
    """
    Remove current SQLAlchemy Session
    """
    storage.close()

if __name__ == '__main__':
    app.run('0.0.0.0', '5000')