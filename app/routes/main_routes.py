from flask import Blueprint, render_template

main_bp = Blueprint("main",__name__,template_folder="templates", static_folder="static")

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/gallerie")
def gallerie():
    return render_template("gallerie.html")