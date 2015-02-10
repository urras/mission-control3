from datetime import datetime
from flask import render_template, Response, session, redirect, url_for
from flask.ext.login import login_required
from . import main
from .. import db
from ..models import User
import pygal

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html', current_time=datetime.utcnow())

