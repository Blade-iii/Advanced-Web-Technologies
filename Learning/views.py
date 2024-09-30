from flask import Blueprint, render_template , redirect , url_for, request # Import libraries from flask
import sqlite3 # import sqllite 3 to create and access a database

views = Blueprint('views', __name__)  # Allows this Python file to be used as a blueprint


connect = sqlite3.connect('database.db')  # Connect to the database
connect.execute(
    'CREATE TABLE IF NOT EXISTS USERS(email TEXT, password TEXT)'
)

@views.route("/")
def home():
    return render_template("index.html") 

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/register" , methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO USERS \
                (email,password) VALUES (?,?)",
                (email,password))
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
    
    

   