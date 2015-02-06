import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY: 'CHANGE THIS'
    SQLALCHEMY_COMMIT_ON_TEARDOWN: True
    
    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG = TRUE
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://' + os.path.join(basedir, 'data.sqlite')


config = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
        }
    
