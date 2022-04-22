import os
from flask import Flask

def create_app(test_config=None):
    """factory function"""
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = b'\xcf\xa1\x94\x9c\xe5\x0b\xa4f\xc5N!\x05Ra\xfc\x9d'

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import search
    from . import show
    app.register_blueprint(search.bp)
    app.register_blueprint(show.bp)

    return app
