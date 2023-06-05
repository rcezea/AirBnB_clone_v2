#!/usr/bin/python3
"""
Start a flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    returns hello at root call
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns hbnb
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    text substitution
    """
    return 'C {}'.format(text).replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_cool(text="is cool"):
    """
    text substitution
    """
    return 'Python {}'.format(text).replace("_", " ")


if __name__ == '__main__':
    app.run('0.0.0.0', '5000')
