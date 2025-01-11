from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .db import db
from .routes import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    CORS(app)

    db.init_app(app)

    from .routes import api_bp
    app.register_blueprint(api_bp)

    return app
