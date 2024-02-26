import os


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = (
        "nvNiTHDWEDyt3ciEJOLauNhSC6szkvGgciTImPeW6F2ThUhtl6yrRmqq4t_co_lP5gQ_sophie"
    )


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")


class ProductionConfig(BaseConfig):
    url = os.environ.get("DATABASE_URL")

    if url is not None and url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = url
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "nvNiTHDWEDyt3ciEJOLauNhSC6szkvGgciTImPeW6F2ThUhtl6yrRmqq4t_co_lP5gQ_sophie",
    )
