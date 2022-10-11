from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Home Page</p>"


@app.route("/about")
def about():
    return "<p>About Page</p>"
