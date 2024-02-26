import os


def test_development_config(test_app):
    test_app.config.from_object("src.config.DevelopmentConfig")
    assert test_app.config["SECRET_KEY"] == (
        "nvNiTHDWEDyt3ciEJOLauNhSC6szkvGgciTImPeW6F2ThUhtl6yrRmqq4t_co_lP5gQ" "_sophie"
    )
    assert not test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")


def test_testing_config(test_app):
    test_app.config.from_object("src.config.TestingConfig")
    assert test_app.config["SECRET_KEY"] == (
        "nvNiTHDWEDyt3ciEJOLauNhSC6szkvGgciTImPeW6F2ThUhtl6yrRmqq4t_co_lP5gQ" "_sophie"
    )
    assert test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
        "DATABASE_TEST_URL"
    )


def test_production_config(test_app):
    test_app.config.from_object("src.config.ProductionConfig")
    assert test_app.config["SECRET_KEY"] == os.getenv(
        "SECRET_KEY",
        "nvNiTHDWEDyt3ciEJOLauNhSC6szkvGgciTImPeW6F2ThUhtl6yrRmqq4t_co_lP5gQ_sophie",
    )  # updated
    assert not test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get("DATABASE_URL")
