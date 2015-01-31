__author__ = 'colinmoore-hill'

import config
import flask
from py2neo import Graph


app = flask.Flask(__name__)
app.secret_key = config.secret_key
graph_db = Graph("http://{{config.NeoUsr}}:{{config.NeoTkn}}:24789/db/data/")
