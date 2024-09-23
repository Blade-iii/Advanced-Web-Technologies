from flask import Flask
from view import views # Import the view.py to use the blueprint

app =  Flask(__name__)
app.register_blueprint(views, url_prefix="/") 

if __name__ == '__main__': # Runs the program by pressing the start button in VS
    app.run(debug=True)

