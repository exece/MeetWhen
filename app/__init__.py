from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
    app=Flask(__name__)

    #we use this utility module to display forms quickly
    bootstrap = Bootstrap(app)

    #A secret key for the session object
    app.secret_key='secret'

    #add Blueprints
    from . import routes
    app.register_blueprint(routes.main)

    
    return app