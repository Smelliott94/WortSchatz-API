from flask_restplus import Namespace, Resource, fields
from flask import jsonify
from flask import current_app
from app import db, translator

api = Namespace('words', description='Words to be added to the database')

wordModel = api.model(
    'Word', {
        'word': fields.String,
        'translation': fields.String
    }
)

class Word(db.Model):
    __tablename__ = "words"

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String())
    translation = db.Column(db.String())

    def __init__(self, word, translation):
        self.word = word
        self.translation = translation

    def __repr__(self):
        return f"<id {id}>"

    def serialize(self):
        return {
            "id": self.id,
            "word": self.word,
            "translation": self.translation
        }

@api.route('/')
class Testing(Resource):

    def get(self):
        words = Word.query.all()
        return jsonify([word.serialize() for word in words])
    
    @api.expect(wordModel)
    def post(self):
        p = api.payload
        word = Word(
            word=p['word'],
            translation=p['translation'] or translator.translate(p['word'], src='de').text
        )
        db.session.add(word)
        db.session.commit()
        return 200