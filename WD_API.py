from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.cors import CORS
from py2neo import Graph
from tests.json.datafile import Cars, Parts

import config
import qrybase


app = Flask(__name__, static_url_path = "")
cors = CORS(app)

app.secret_key = config.secret_key
graph_db = Graph("http://{{config.NeoUsr}}:{{config.NeoTkn}}:24789/db/data/")


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/car')
def getCars():
    # carAPI = graph_db.cypher.execute(qrybase.allCars)
    # print carAPI
    return 'Hello Cars !'


@app.route('/part')
def getPart():
    # partAPI = graph_db.cypher.execute(qrybase.allParts)
    # print partAPI
    return 'Hello Parts !'




if __name__ == '__main__':
    app.run()
