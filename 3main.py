from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route("/")
def home():
    return render_template("home.html",current_time=datetime.utcnow())

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/ash")
def ash():
    return "Hello, Ash!"

if __name__ == "__3main__":
    app.run(debug=True)
