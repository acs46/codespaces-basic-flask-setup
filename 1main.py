from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/ash")
def ash():
    return "Hello, Ash!"

if __name__ == "__1main__":
    app.run(debug=True)
