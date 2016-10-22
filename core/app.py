# -*- coding: utf-8 -*-

from flask import Flask

from core.models import db
from core.api import blueprint


def create_app(config=None):
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_ECHO"] = True
    app.register_blueprint(blueprint)

    db.init_app(app)

    # Should be in configure file
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

    return app
