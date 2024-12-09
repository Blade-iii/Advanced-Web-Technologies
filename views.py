from flask import Blueprint, render_template , redirect , url_for, request, flash,session # Import libraries from flask
import sqlite3 # import SQLite 3 to create and access a database
import json # Import Json Library
from flask_bcrypt import Bcrypt # Encryption for the users password
import datetime

bcrypt = Bcrypt()
views = Blueprint('views', __name__)  # Allows this Python file to be used as a blueprint

# Connect to the database and create the user table and the game table
connect = sqlite3.connect('database.db')  
connect.execute(
    'CREATE TABLE IF NOT EXISTS USERS(userID INTEGER PRIMARY KEY AUTOINCREMENT,email TEXT NOT NULL UNIQUE, password TEXT NOT NULL UNIQUE, personName TEXT NOT NULL)'
)
connect.execute(
    'CREATE TABLE IF NOT EXISTS GAMES(gameID INTEGER PRIMARY KEY,gameName TEXT NOT NULL,gameReleaseDate TEXT NOT NULL, gameAgeRating INTEGER NOT NULL, gameDeveloper TEXT NOT NULL, gamePlatforms TEXT NOT NULL, gameDescription TEXT NOT NULL, gameUserRating REAL, gameActors TEXT NOT NULL, gamePoster TEXT, gameTrailer TEXT )'
)

cursor = connect.cursor()

# Query data from SQLite table
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Convert data to JSON
data = []
for row in rows:
    data.append({'id': row[0], 'email': row[1], 'password': row[2], 'name':row[3]})

# Dump JSON data to a file this is used to show that users can register
with open('users.json', 'w') as f:
    json.dump(data, f, indent=4)

connect.close();

   # Load the JSON data from the file
with open("games.json", "r") as file:
    data = json.load(file)
    gamesList = data["Games"]
  
# The games from the Json are then put into the games database      
with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.executemany(
    "INSERT OR IGNORE INTO GAMES(gameID, gameName, gameReleaseDate, gameAgeRating, gameDeveloper, gamePlatforms, gameDescription, gameUserRating, gameActors, gamePoster,gameTrailer) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)",
    [[d.get('gameID'), d.get('gameName'), d.get('gameReleaseDate'), d.get('gameAgeRating'), d.get('gameDeveloper'), d.get('gamePlatforms'), d.get('gameDescription'), d.get('gameUserRating'), d.get('gameActors'), d.get('gamePoster', None), d.get('gameTrailer', None)] for d in gamesList]
)

# Root directory for the website
@views.route("/")
def home():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM GAMES ORDER BY gameReleaseDate DESC LIMIT 3')
        gameData = cursor.fetchall()
    
    if gameData:
         ## Put the data from games into an list
        keys = ["gameID", "gameName", "gameReleaseDate", "gameAgeRating", "gameDeveloper", "gamePlatforms", "gameDescription", "gameUserRating", "gameActors","gamePoster","gameTrailer"]
        gameDataList = [dict(zip(keys, games)) for games in gameData]
        
    return render_template("index.html",games=gameDataList) 

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
        
        # Encrypt password with hashing
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
        # Insert registered user details into the database
        with sqlite3.connect("database.db") as users:
            cursor = users.cursor()
            cursor.execute("INSERT INTO USERS \
                (userID,email,password,personName) VALUES (?,?,?,?)",
                (userID,email,pw_hash,name))
            users.commit()
            return redirect(url_for("views.home"))
    else:
         # Display an error message
         flash('Error. Please try again.', 'danger')
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
            session['userID'] = result[0]
            
            if bcrypt.check_password_hash(storedPw, password):
             # If the credentials are correct, redirect to the home page
                return redirect(url_for("views.home"))
        
            else:
            # If incorrect, display an error message
                flash('Incorrect email or password. Please try again.', 'danger')
                return redirect(url_for("views.login"))
        else:
            flash('Incorrect email or password. Please try again.', 'danger')
            return redirect(url_for("views.login"))
   
    return render_template('login.html')

# Logout directory which removes session data and redirects the user
@views.route("/logout/")
def logout():
    if session['userName'] is None:
        return redirect(url_for("views.home"))
    else:
        session.pop('userName', None)
        return redirect(url_for("views.home"))
    
@views.route("/settings")
def settings():
    if session['userID']:
        userID = session['userID']
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM USERS WHERE userID=?', (userID,))
        userData = cursor.fetchone()
    else:
        redirect(url_for("views.home"))
        
    if userData:
        keys=["userID","email","password","name"]
        userList = dict(zip(keys,userData))
    
        return render_template("settings.html",user=userList)
    else:
        redirect(url_for("views.home"))
    
   
# Game directory this allows the user to click on a game and view its details 
@views.route("/games/")
def games():
    # Get the id from the url
    id = request.args.get('id','') 
    
    # Check if the id was passed in
    if id:
        connect = sqlite3.connect('database.db') 
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM GAMES WHERE gameID=?',(id,))
        gameData = cursor.fetchone()
        
    # If there are games pulled from the database then it continues to put the game         
    if gameData:
        keys = ["gameID", "gameName", "gameReleaseDate", "gameAgeRating", "gameDeveloper", "gamePlatforms", "gameDescription", "gameUserRating", "gameActors","gamePoster","gameTrailer"]
       
        # Assign the data from the database with the keys to be accessed
        gameDataDict = dict(zip(keys, gameData))
        
        # If game data is found redirect with game data
        return render_template('game.html',game=gameDataDict)
    else:  
        # If no game id redirect to home
        return render_template('index.html')

# This directory shows all games that are in the database   
@views.route("/allGames/")
def allGames():
    connect = sqlite3.connect('database.db') 
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM GAMES ORDER BY gameName ASC')
    gameData = cursor.fetchall()
    
    # If games are found it will display the games
    if gameData:
        ## Put the data from games into an list
        keys = ["gameID", "gameName", "gameReleaseDate", "gameAgeRating", "gameDeveloper", "gamePlatforms", "gameDescription", "gameUserRating", "gameActors","gamePoster","gameTrailer"]
        gameDataList = [dict(zip(keys, game)) for game in gameData]
        
        # Page logic for loading more pages
        page = int(request.args.get('page',1))
        # Number of games to be displayed
        gamesPerPage = 12
        # Start index so if the page number is 3 then the starting index will be 24 2*12=24
        startIndex = (page-1) * gamesPerPage
        # Calculates endIndex
        endIndex = startIndex + gamesPerPage
        # Splice the list with start and end index to make sure only 12 games are displayed at once
        games = gameDataList[startIndex:endIndex]
        # Calculate total pages and make sure its a whole number
        totalPages = (len(gameDataList) + gamesPerPage -1) // gamesPerPage
        # Stores the size of the array in a session
        session['gameSize'] = len(gameDataList)
        
        # If game data is found redirect with game data and page data
        return render_template('gameCatalog.html',games=games,currentPage=page,totalPages=totalPages)
    else:  
        # If no game id redirect to home
        return render_template('index.html')
    
# Directory for copyright information for the website
@views.route("/copyright/")
def copyright():
    return render_template('copyright.html')

# Directory for privacy information for the website
@views.route("/privacy/")
def privacy():
    return render_template('privacy.html')

# Directory for terms information for the website
@views.route("/terms/")
def terms():
    return render_template('terms.html')

# Directory for search it allows the user to search for games throughout the website
@views.route("/search" , methods=['GET', 'POST'])
def search():
    if request.method =='POST':
        search = request.form.get('search')

        # If theres a value in search continue
        if search:
            connect = sqlite3.connect('database.db') 
            cursor = connect.cursor()
            # Check if theres game in the database with the name the user inputted
            cursor.execute('SELECT * FROM GAMES WHERE gameName LIKE ?', ('%' + search + '%',)) 
            searchData = cursor.fetchall()

            # Assign keys 
            keys = ["gameID", "gameName", "gameReleaseDate", "gameAgeRating", "gameDeveloper", "gamePlatforms", "gameDescription", "gameUserRating", "gameActors","gamePoster","gameTrailer"]
            # Assign keys and values to gameDataSearch
            gameDataSearch = [dict(zip(keys, searchGames))for searchGames in searchData ]

            return render_template('search.html', games=gameDataSearch)
        
        else:
            flash('No Game found.', 'danger')
            return redirect(url_for('views.home'))
    else:
        return redirect(url_for('views.home'))
    
@views.route("/remove")
def remove():
    if session['userID']:
        userID = session['userID']
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        
        cursor.execute("DELETE FROM USERS WHERE userID=?",((userID,)))
        connect.commit()
        connect.close()
    return redirect(url_for("views.logout"))

@views.route("/update" , methods=['GET', 'POST'])
def update():
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        
          # Encrypt password with hashing
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
        if session['userID']:
            userID = session["userID"]
            connect = sqlite3.connect('database.db')
            cursor = connect.cursor()
            
            cursor.execute("UPDATE USERS SET email=?, password=?, personName=? WHERE userID=?",((email,pw_hash,name,userID,)))
            connect.commit()
            connect.close()
        else:
            return redirect(url_for("views.home"))
    
    return render_template("update.html")

