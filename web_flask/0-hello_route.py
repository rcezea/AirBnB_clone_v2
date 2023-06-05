#!/usr/bin/python3
"""
Start a flask web application that:
listens on 0.0.0.0 port 5000
displays "Hello HBNB!"
use strict_slashes=Fale
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    returns hello at root call
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run('0.0.0.0', '5000')
