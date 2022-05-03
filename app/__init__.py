from flask import Flask
from flask_bootstrap import Bootstrap5
from config import config_options


bootstrap = Bootstrap5()

def create_app(config_name):
    app = Flask(__name__)
    # Initalizing bootstrap
    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .requests import configure_request
    configure_request(app)

    return app