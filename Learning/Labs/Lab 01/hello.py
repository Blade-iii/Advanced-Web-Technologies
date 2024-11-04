from flask import Flask # Import the flask library
app = Flask(__name__) # Name for the application

@app.route('/')
def hello_world(): # Function that returns hello napier
    return'Hello Napier'
