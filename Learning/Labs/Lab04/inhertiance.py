from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def inheritance():
    return render_template('base.html')

@app.route("/inherits1")
def inherits1():
    return render_template('inheritance1.html')

@app.route("/inherits2")
def inherits2():
    return render_template('inhertiance2.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)