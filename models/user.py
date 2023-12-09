from flask_login import UserMixin
from mongoengine import *
from werkzeug.security import generate_password_hash, check_password_hash

connect("deneme")
# Error Handling
try:
    connect("deneme")
    print("succesfully connected!")
except Exception as error:
    print("unseccesfully process:", error)


class User(UserMixin, Document):
    username = StringField(required=True, max_length=64)
    email = StringField(required=True)
    password = StringField()

    # Password Hashing
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Password Checking
    def check_password(self, password):
        return check_password_hash(self.password, password)
