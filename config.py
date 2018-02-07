import os


class Config:
    """
    Parent Config
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:Sam@localhost/blog'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
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
    DEBUG = True


class TestConfig(Config):
    """
    Child Config with test configurations
    """
    pass


config_options = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}
