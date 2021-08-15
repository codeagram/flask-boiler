""" Configurations """

import os


basedir = os.path.abspath(os.path.dirname(__name__))


class BaseConfig:

    "Base config class"

    SECRET_KEY = (
        os.environ.get("SECRET_KEY")
        or "509fd5a3dfe665383d7a9539be258a5c872f7b6b3d713fcd99f227e406f228cfi"
    )
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):

    "Production specific config"

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URI")


class TestingConfig(BaseConfig):

    "Staging specific config"

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI") or "sqlite:///"


class DevelopmentConfig(BaseConfig):

    "Development environment specific config"

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEV_DATABASE_URI"
    ) or "sqlite:///" + os.path.join(basedir, "data-dev.db")
