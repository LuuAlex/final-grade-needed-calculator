from flask import Blueprint, render_template, jsonify

views = Blueprint(__name__, "view")


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/json")
def get_json():
    return jsonify({'id': 1})
