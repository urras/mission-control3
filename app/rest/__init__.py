from flask import Blueprint
from ..models import TelemData, ChartRender

rest = Blueprint('rest', __name__)
data = TelemData()
render = ChartRender()

from . import views
