from flask import Blueprint, render_template

main = Blueprint('main', __name__) 

@main.route('/')
def about():
    return render_template("about.html")

@main.route('/docs')
def docs():
    return render_template("docs.html")

