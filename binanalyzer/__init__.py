__version__ = '0.1'
from flask import Flask

app = Flask('binanalyzer')
app.config['SECRET_KEY'] = 'random'
app.debug = False
from binanalyzer.controllers import *
