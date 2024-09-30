from flask import Blueprint, render_template , redirect , url_for, Request

views = Blueprint('views', __name__)  # Allows this Python file to be used as a blueprint

@views.route("/")
def home():
    return render_template("index.html") 

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/register")
def register():
    if request.method == 'POST':
        

    return render_template("register.html")