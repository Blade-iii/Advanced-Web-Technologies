from flask import Blueprint, render_template 

views = Blueprint(__name__,"views") # ALlows this py file to be used as a blueprint

@views.route("/")
def home():
    return render_template("index.html", name="Thomas", age=21) # PAss variables and html files

@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html",name=username)