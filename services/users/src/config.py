import os


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = (
        "nvNiTHDWEDyt3ciEJOLauNhSC6szkvGgciTImPeW6F2ThUhtl6yrRmqq4t_co_lP5gQ_sophie"
    )
    BCRYPT_LOG_ROUNDS = 13  # new


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    BCRYPT_LOG_ROUNDS = 4  # new


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")
    BCRYPT_LOG_ROUNDS = 4  # new


class ProductionConfig(BaseConfig):
    url = os.environ.get("DATABASE_URL")

    if url is not None and url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = url
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "nvNiTHDWEDyt3ciEJOLauNhSC6szkvGgciTImPeW6F2ThUhtl6yrRmqq4t_co_lP5gQ_sophie",
    )
