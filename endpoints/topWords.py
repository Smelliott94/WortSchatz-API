from flask_restplus import Namespace, Resource
from flask import jsonify

api = Namespace('topWords',
    description='Interface for generating or entering the top words for a lesson')

@api.route('/')
class WordList(Resource):

    def get(self):
        return jsonify([
    {
      'id': 1,
      'word': 'ein',
      'translation': 'one'
    },
    {
      'id': 2,
      'word': 'zwei',
      'translation': 'two'
    },
    {
      'id': 3,
      'word': 'drei',
      'translation': 'three'
    },
    {
      'id': 4,
      'word': 'vier',
      'translation': 'four'
    },
    {
      'id': 5,
      'word': 'funf',
      'translation': 'five'
    },
    {
      'id': 6,
      'word': 'sechs',
      'translation': 'six'
    },
    {
      'id': 7,
      'word': 'sieben',
      'translation': 'seven'
    },
    {
      'id': 8,
      'word': 'acht',
      'translation': 'eight'
    }
])