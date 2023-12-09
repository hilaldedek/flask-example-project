print("hello world")
from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
import pymongo

from models.user import User

client = pymongo.MongoClient("mongodb://localhost:27017/?directConnection=true")
myDb = client["deneme"]
col = myDb["User"]
# print(client.list_database_names())
# print(myDb.list_collection_names())
# col.insert_one({"name": "cemile", "surname": "salakmisin", "age": "25"})
# x = {"age": "25"}
# y = col.find(x)
# for i in y:
#     print(x)
app = Flask(__name__)

app.config[
    "SECRET_KEY"
] = "P4plITOLXjptPtXHK2h8dWtrBFxc70X0pi6rE2uUDnyV4ndBGfuVVPsP1fiGwmVo"


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
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        new_user = User(
            email=f"{email}", username=f"{username}", password=f"{password}"
        )
        new_user.set_password(password)
        new_user.save()
        return render_template("welcome.html", name=username)

    else:
        return render_template("post.html")


@app.route("/post/<url>")
def post(url):
    return render_template("post.html", url=url)


# error handling
@app.errorhandler(404)
def pageNotFound(error):
    return render_template("error.html")
