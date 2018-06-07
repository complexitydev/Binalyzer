__version__ = '0.1'
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
app = Flask('binanalyzer')
app.config['SECRET_KEY'] = 'random'
app.debug = False
from binanalyzer.controllers import *