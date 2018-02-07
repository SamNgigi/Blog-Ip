import os


class Config:
    """
    Parent Config
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # pass


class ProdConfig(Config):
    """
    Child Config with production configurations
    """
    pass


class DevConfig(Config):
    """
    Child Config with development configurations
    """
    pass


class TestConfig(Config):
    """
    Child Config with test configurations
    """
    pass
