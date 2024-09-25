from flask import Blueprint, render_template , jsonify , redirect , url_for

views = Blueprint('views', __name__)  # Allows this Python file to be used as a blueprint

@views.route("/")
def home():
    return render_template("index.html") 