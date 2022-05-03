from flask import Flask
from flask_bootstrap import Bootstrap5
# from app.config import DevConfig
from config import config_options
# from app.main import errors
# from app.main import views

bootstrap = Bootstrap5()

def create_app(config_name):
    app = Flask(__name__)
    # Initalizing bootstrap
    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)

    # Initalizing the config file containig the API key
    # app.config.from_pyfile('config.py')
    # app.config.from_object(DevConfig)
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .requests import config_request
    config_request(app)

    return app