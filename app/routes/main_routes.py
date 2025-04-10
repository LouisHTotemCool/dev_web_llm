from flask import Blueprint, render_template, current_app
import os


main_bp = Blueprint("main",__name__,template_folder="templates", static_folder="static")

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/gallerie")
def gallerie():
    file_names = sorted(os.listdir('app/static/img'))
    current_app.logger.info(file_names)
    
    img_path = ['../static/img/' + x for x in file_names]
    current_app.logger.info(img_path)

    return render_template("gallerie.html", files_path=img_path)