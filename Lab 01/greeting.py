from flask import Flask
app = Flask (__name__)

@app.route("/")
def greet():
    return "Greetings Traveller"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/goodbye")
def goodbye():
    return "Goodbye :( "

if __name__ == "__main__":
    app.run(host='0.0.0.0')