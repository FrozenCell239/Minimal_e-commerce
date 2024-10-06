from app.extensions import db, csrf
from config import Config
from flask import Flask

def create_app(config_class = Config):
    # App initialisation
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Flask extensions initialisation
    db.init_app(app)
    csrf.init_app(app)

    # Blueprints initialisation
    from app.main import main_bp
    app.register_blueprint(main_bp)
    from app.product import product_bp
    app.register_blueprint(product_bp, url_prefix = '/product')
    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix = '/api')
    csrf.exempt(api_bp)

    # App ready
    return app