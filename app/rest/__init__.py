from flask import Blueprint
from ..models import TelemData

rest = Blueprint('rest', __name__)
data = TelemData()

from . import views
