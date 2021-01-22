import os

from flask import Flask
from flask import render_template

# DB object to work with
from application.utils.database import db
# Services
# Users service
from application.services.users.views import user_bp


def create_tables(app) -> None:
    """
    Need this function to create all tables from ALL modes in app.

    IMPORTANT: we need to import ALL models here (before usging create_all() method),
    otherwise, "db" object won't see our models and will ignore creating actual tables.

    :return: None
    """
    db.init_app(app)
    with app.app_context():
        from application.services.users.models import User
        db.create_all()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(
        app.instance_path, 'web_money_manager_DB.sqlite'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # todo: have no clue what is it

    # register blueprints
    app.register_blueprint(user_bp)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    create_tables(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
