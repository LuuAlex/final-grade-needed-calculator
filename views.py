# DEPRECIATED
"""
import json
from flask import Blueprint, render_template, request

views = Blueprint(__name__, "view")


@views.route("/")
def home():
    result = get_post_javascript_data()  # menu.getResult()
    return render_template("home.html", result=result)


@views.route('/postmethod', methods=['POST'])
def get_post_javascript_data():
    jsdata = request.form['javascript_data']
    return json.loads(jsdata)[0]



@views.route("/json")
def get_json():
    return jsonify({'id': 1})
"""
