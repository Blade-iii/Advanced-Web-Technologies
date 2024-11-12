from flask import Flask , url_for, redirect,render_template
from views import views # Import the view.py to use the blueprint
from flask import Flask
from flask_bcrypt import Bcrypt

app =  Flask(__name__)
bcrypt = Bcrypt(app)

app.register_blueprint(views, url_prefix="/") 

if __name__ == '__main__': # Runs the program by pressing the start button in VS
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0', port=5000, debug=True)

