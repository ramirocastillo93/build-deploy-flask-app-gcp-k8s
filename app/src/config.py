import os
basedir = os.path.abspath(os.path.dirname(__file__))

db_user = os.environ['POSTGRES_USER']
db_pass = os.environ['POSTGRES_PASSWORD']
db_host = os.environ['POSTGRES_HOST']
db_name = os.environ['POSTGRES_DB']
db_port = os.environ['POSTGRES_PORT']

class Config(object):
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False
    CSRF_ENABLED = False
    SECRET_KEY = ""
    SQLALCHEMY_DATABASE_URI = f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}'

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEBUG = True
    DEVELOPMENT = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True