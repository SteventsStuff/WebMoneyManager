import os

from flask import Flask
from flask import render_template
from flask_login import login_required
from flask_debugtoolbar import DebugToolbarExtension

# Configs
from application import config
# Object to work with DB
from application.utils.database import db
# Services
from application.services.users.views import user_bp
# Helpers
from application.utils.login import login
from application.utils.migrate import migrate
from application.utils.helpers.custom_exceptions import IncorrectEnvSet
from application.utils.helpers.view_helper import sign_in_required


def create_tables(app) -> None:
    """
    Need this function to create all tables from ALL modes in app.

    IMPORTANT: we need to import ALL models here (before usging create_all() method),
    otherwise, "db" object won't see our models and will ignore creating actual tables.

    :return: None
    """
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    # create app
    app = Flask(__name__, instance_relative_config=True)

    # select ENV
    if os.environ.get('FLASK_ENV') == 'development':
        cfg = config.DevelopmentConfig()
    elif os.environ.get('FLASK_ENV') == 'production':
        cfg = config.ProductionConfig()
    elif os.environ.get('FLASK_ENV') == 'testing':
        cfg = config.TestingConfig()
    else:
        raise IncorrectEnvSet('Incorrect ENV was set!')
    # configure the app
    app.config.from_object(cfg)
    # additional configs
    app.config['SQLALCHEMY_DATABASE_URI'] = cfg.DATABASE_URI

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # create tables in Database
    create_tables(app)

    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'user_service.sign_in'

    # debug
    toolbar = DebugToolbarExtension(app)

    # register blueprints
    app.register_blueprint(user_bp)

    # a simple page that says hello
    @app.route('/')
    @login_required
    def index():
        return render_template('index.html')

    return app
