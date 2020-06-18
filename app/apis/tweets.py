#from flask_restplus import Namespace, Resource, fields
from flask_restx import Namespace, Resource, fields
from app.db import tweet_repository

api = Namespace('tweets')


#All models instantiated with model(), clone() and inherit() will be automatically documented in your Swagger specifications.
model = api.model('Tweet', {
    'id': fields.Integer,
    'text': fields.String,
    'created_at': fields.DateTime(dt_format='rfc822'),
})

@api.route('/<int:id>')
@api.response(404, 'Tweet not found')

class TweetResource(Resource):
    @api.marshal_with(model)
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404)
        else:
            return tweet
