from flask import Flask, url_for , request

app = Flask(__name__)

@app.route("/hello")
def hello():
    name = request.args.get('name','')   
    if name == '':
        return"no parm supplied"
    else:
        return "Hello %s" % name


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
