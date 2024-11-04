from flask import Blueprint, render_template , redirect , url_for, request, flash # Import libraries from flask
import sqlite3 # import SQLite 3 to create and access a database
import json # Import Json Library
views = Blueprint('views', __name__)  # Allows this Python file to be used as a blueprint

# Connect to the database and create the user table
connect = sqlite3.connect('database.db')  
connect.execute(
    'CREATE TABLE IF NOT EXISTS USERS(userID INTEGER PRIMARY KEY AUTOINCREMENT,email TEXT, password TEXT, personName TEXT)'
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
        
        
        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO USERS \
                (email,password,personName,userID) VALUES (?,?,?,?)",
                (email,password,name,userID))
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
            cursor.execute('SELECT * FROM USERS WHERE email = ? AND password = ?', (email, password))
            result = cursor.fetchone()  # Fetch the user record
        
        if result:
            flash('Login Successful')
            # If the credentials are correct, redirect to the home page
            return redirect(url_for('views.home'))
        
        else:
            # If incorrect, display an error message
            flash('Incorrect email or password. Please try again.', 'danger')
            return render_template('login.html')
    
    return render_template('login.html')
    

 
        