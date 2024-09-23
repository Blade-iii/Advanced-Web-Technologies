from flask import Blueprint, render_template , jsonify , redirect , url_for

# Jsonify for jsons
# redirect and url_for is for redirect

views = Blueprint('views', __name__)  # Allows this Python file to be used as a blueprint

@views.route("/")
def home():
    return render_template("index.html", name="Thomas", age=21) # PAss variables and html files

@views.route("/profiles/<username>")
def profiles(username):
    return render_template("index.html",name=username)

@views.route("/profile")
def profile():
    return render_template("profile.html")


@views.route("/json") # Returns a Json
def get_json():
    return jsonify({'name' : 'tom', 'pog': 10})

""" @views.route("/data")
def get_data():
    data = request.json
    return jsonify(data) """
    
@views.route("/go-home") # Redirect
def go_to_home():
    return redirect(url_for('views.home'))