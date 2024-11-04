from flask import Blueprint, render_template , redirect , url_for, request, flash # Import libraries from flask
import sqlite3 # import sqllite 3 to create and access a database

views = Blueprint('views', __name__)  # Allows this Python file to be used as a blueprint


connect = sqlite3.connect('database.db')  # Connect to the database
connect.execute(
    'CREATE TABLE IF NOT EXISTS USERS(userID INTEGER PRIMARY KEY AUTOINCREMENT,email TEXT, password TEXT, personName TEXT)'
)

@views.route("/")
def home():
    return render_template("index.html") 

@views.route("/about")
def about():
    return render_template("about.html")

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
     
     
@views.route("/participants") 
def participants(): 
        connect = sqlite3.connect('database.db') 
        cursor = connect.cursor() 
        cursor.execute('SELECT * FROM USERS') 
  
        data = cursor.fetchall() 
        return render_template("participants.html", data=data) 
    
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
    

 
        