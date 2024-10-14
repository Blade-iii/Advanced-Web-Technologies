from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def users():
    names = ['Thomas','Ben','Steve','Bob','Ryan']
    return render_template('loopNames.html', names=names)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)