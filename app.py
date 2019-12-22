from flask import Flask
from flask_restplus import Api
from endpoints import topWords

from endpoints.topWords import api as topWords

app = Flask(__name__)
api = Api(app, version='ALPHA', title='Wortschatz',
    description='Smart vocab tracking for German lessons')

api.add_namespace(topWords)

@app.after_request
def cors_headers(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    print(response.headers)
    return response