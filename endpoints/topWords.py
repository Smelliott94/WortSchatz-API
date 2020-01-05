from flask_restplus import Namespace, Resource
from flask import jsonify

api = Namespace('topWords',
    description='Interface for generating or entering the top words for a lesson')

@api.route()
class WordList(Resource):

    def get(self)
        
        return jsonify([
    {
      'id': 0,
      'word': 'ein',
      'translation': 'one'
    },
    {
      'id': 1,
      'word': 'zwei',
      'translation': 'two'
    },
    {
      'id': 2,
      'word': 'drei',
      'translation': 'three'
    },
    {
      'id': 3,
      'word': 'vier',
      'translation': 'four'
    },
    {
      'id': 4,
      'word': 'funf',
      'translation': 'five'
    },
    {
      'id': 5,
      'word': 'sechs',
      'translation': 'six'
    },
    {
      'id': 6,
      'word': 'sieben',
      'translation': 'seven'
    },
    {
      'id': 7,
      'word': 'acht',
      'translation': 'eight'
    }
])