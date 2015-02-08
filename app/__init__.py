from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config

#Initialize object methods
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong' #Verify UserAgent & IP address of returning users
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app
    
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    #Register main web interface as blueprint
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Register authentication system as blueprint under /auth (/login would be /auth/login)
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    #Register chart rendering front
    from charts import charts as charts_blueprint
    app.register_blueprint(charts_blueprint, url_prefix='/charts')

    return app
