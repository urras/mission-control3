from flask import render_template, redirect, request, url_for, jsonify
from flask.ext.login import login_required
from . import rest, data, render
from flask import Response
from ..models import TelemData, mongo_jsonify
import pygal
from pygal.style import Style
import json
from datetime import datetime



@rest.route('/charts.json', methods=['GET', 'POST'])
def generate_charts():
    name = data.fixTime(data.getField("timestamp"))
    return render.renderChart('Line', "CPU Power", data.getField("cdh", "cpu_usage"), x_name=name)
