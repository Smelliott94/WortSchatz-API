from flask import Flask
import os
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from googletrans import Translator

app = Flask(__name__)
translator = Translator()
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api = Api(
    app,
    version='ALPHA',
    title='Wortschatz',
    description='Smart vocab tracking for German lessons'
    )

from endpoints.topWords import api as topWords
from endpoints.words import api as words
api.add_namespace(topWords)
api.add_namespace(words)

@app.after_request
def cors_headers(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    print(response.headers)
    return response
