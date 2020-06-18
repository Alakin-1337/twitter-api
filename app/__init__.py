"""
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .main.controllers import main
    app.register_blueprint(main)

    return app
"""

from flask import Flask
from flask_restx import Api

from .db import tweet_repository
from .models import Tweet
tweet_repository.add(Tweet("a first tweet"))
tweet_repository.add(Tweet("a second tweet"))

def create_app():
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return "Goodbye World!"

    from .apis.tweets import api as tweets
    api = Api()
    api.add_namespace(tweets)
    api.init_app(app)

    app.config['ERROR_404_HELP'] = False
    return app
