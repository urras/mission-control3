import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'CHANGE THIS'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MONGO_HOST = 'localhost'
    MONGO_PORT = '27017'

    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/data-dev.sqlite')
    MONGO_DBNAME = 'glados_data_dev'
    COM = 'Simulate'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/data.sqlite')
    MONGO_DBNAME = 'glados_data'
    COM = 'Serial'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/data-test.sqlite')
    MONGO_DBNAME = 'glados_data_test'
    COM = 'Serial'

config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig,
        'default': DevelopmentConfig
        }
    
