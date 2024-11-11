from flask import Blueprint, render_template , redirect , url_for, request, flash,session # Import libraries from flask
import sqlite3 # import SQLite 3 to create and access a database
import json # Import Json Library
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
views = Blueprint('views', __name__)  # Allows this Python file to be used as a blueprint

# Connect to the database and create the user table
connect = sqlite3.connect('database.db')  
connect.execute(
    'CREATE TABLE IF NOT EXISTS USERS(userID INTEGER PRIMARY KEY AUTOINCREMENT,email TEXT NOT NULL UNIQUE, password TEXT NOT NULL UNIQUE, personName TEXT NOT NULL)'
)
connect.execute(
    'CREATE TABLE IF NOT EXISTS GAMES(gameID INTEGER PRIMARY KEY,gameName TEXT NOT NULL,gameReleaseDate DATE NOT NULL, gameAgeRating INTEGER NOT NULL, gameDeveloper TEXT NOT NULL, gamePlatforms TEXT NOT NULL, gameDescription TEXT NOT NULL, gameUserRating REAL, gameActors TEXT NOT NULL )'
)

cursor = connect.cursor()

# Query data from SQLite table
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Convert data to JSON
data = []
for row in rows:
    data.append({'id': row[0], 'email': row[1], 'password': row[2], 'name':row[3]})

# Dump JSON data to a file
with open('users.json', 'w') as f:
    json.dump(data, f, indent=4)

# Root directory for the website
@views.route("/")
def home():
    return render_template("index.html") 

# About directory for the website to explain what it's about
@views.route("/about")
def about():
    return render_template("about.html")

# Register directory for the website to allow the user to register
@views.route("/register/" , methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        userID = None
        
    # Encrypt password
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO USERS \
                (userID,email,password,personName) VALUES (?,?,?,?)",
                (userID,email,pw_hash,name))
            users.commit()
            return render_template("index.html")
    else:
         return render_template("register.html")
  
# Login directory to allow the user to login to the website       
@views.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Connect to the database and check if the user exists
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM USERS WHERE email = ?', (email,))
            result = cursor.fetchone()  # Fetch the user record
           
        
        if result:
            storedPw = result[2]
            session['userName'] = result[3] # Store user name in a session
            if bcrypt.check_password_hash(storedPw, password):
                flash('Login Successful')
             # If the credentials are correct, redirect to the home page
                return render_template('index.html',userName = session['userName'])
        
        else:
            # If incorrect, display an error message
            flash('Incorrect email or password. Please try again.', 'danger')
            return render_template('login.html')
    
    return render_template('login.html')

@views.route("/logout/")
def logout():
    if session['userName'] != None:
        session.pop('userName', None)
        return render_template('index.html')
    else:
        return render_template('index.html')
    
@views.route("/games/")
def games():

   # Load the JSON data from the file
    with open("games.json", "r") as file:
        data = json.load(file)

    # Pass the data to the template
    return render_template("game.html", games=data['Games'])

        