""" Top level application module """

import os
from flask import Flask


def create_app():

    """ Application Factory """

    app = Flask( __name__)


    environ = app.config["ENV"]

    if environ == "development":
        app.config.from_object("config.DevelopmentConfig")

    elif environ == "testing":
        app.config.from_object("config.TestingConfig")

    else:
        app.config.from_object("config.ProductionConfig")


    return app
