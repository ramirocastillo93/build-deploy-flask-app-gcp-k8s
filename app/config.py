import os
basedir = os.path.abspath(os.path.dirname(__file__))

db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']
db_host = os.environ['DB_HOST']
db_name = os.environ['DB_NAME']

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