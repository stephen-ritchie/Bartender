import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

__version__ = 1.0
db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'db.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    with app.app_context():

        from .models import Pump

        db.init_app(app)
        db.create_all()

        # Include routes
        from .views import main

        # Register blueprints
        app.register_blueprint(main.main_bp)

        return app
