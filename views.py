from flask import Blueprint

views = Blueprint(__name__, "view")


@views.route("/")
def home():
    return "home page"
