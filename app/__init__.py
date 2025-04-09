from flask import Flask
from .routes.main_routes import main_bp
from flask import url_for

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)

    return app

