from flask import Flask
from flask_cors import CORS
from routes.helloworld import helloworld_bp


def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(helloworld_bp)
    CORS(app, supports_credentials=True)
    return app