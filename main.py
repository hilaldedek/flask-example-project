print("hello world")
from flask import Flask, render_template, request, url_for


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", username=name)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/post/<url>")
def post(url):
    return render_template("post.html", url=url)


# error handling
@app.errorhandler(404)
def pageNotFound(error):
    return render_template("error.html")
