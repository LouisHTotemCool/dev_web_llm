from flask import Blueprint, render_template, current_app
import os
import ollama

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



    ollama.pull('gemma3:12b')
    response = ollama.chat(model='gemma3:12b', 
    messages=[{
        'role': 'user', 
        'content': "Raconte une histoire effrayante en t'inspirant de l'image, l'histoire doit faire 3 phrases.",
        'images': ["app/static/img/4pote.jpg"]
    }],
    # options={"temperature":0.7}
    )

    return render_template("gallerie.html", files_path=img_path, rep=response)


    