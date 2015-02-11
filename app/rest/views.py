from flask import render_template, redirect, request, url_for, jsonify
from flask.ext.login import login_required
from . import rest, data
from flask import Response
from ..models import TelemData, mongo_jsonify
import pygal
import json

@rest.route('/test', methods=['GET', 'POST'])
def test():
    line_chart = pygal.Line()
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    return line_chart.render_response()

@rest.route('/test2')
def test2():
    data = TelemData()
    #return mongo_jsonify(data.getField("power.top2_voltage", 1))
    return mongo_jsonify(data.getMostRecent())

@rest.route('/charts.json', methods=['GET', 'POST'])
def generate_charts():
    cdh_chart = pygal.Line()
    cdh_chart.title = "CDH"
    data.getField("sdfsdf")
    cdh_chart.x_labs = data.getField("timestamp")
    cdh_chart.add('CPU Usage', data.getField("cdh", "cpu_usage"))
    print data.getField("cdh", "cpu_usage")
    return Response(str(cdh_chart.render()), mimetype="text/plain")
