print("hello world")
from flask import Flask, jsonify, render_template, request, url_for
import pymongo


app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]


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


@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        req_Json = request.json
        username = req_Json["username"]
        email = req_Json["email"]
        password = req_Json["password"]
        return jsonify({"response": "welcome" + username + email + password})

    else:
        return jsonify({"response": "get request called"})


@app.route("/post/<url>")
def post(url):
    return render_template("post.html", url=url)


# error handling
@app.errorhandler(404)
def pageNotFound(error):
    return render_template("error.html")
