from flask import session
from bson.objectid import ObjectId

from great import db

class User():
    def __init__(self, id=0, name="", email="", password=""):
        self.id = id
        self.name = name
        self.email = email
        self.password = password


    def signUpUser(self, user=None):
        try:
            db.users.insert({
                "name": user.name,
                "email": user.email,
                "password": user.password
            })

            return True;

        except:
            return False;


    def loginUser(self, email="", password=""):
        user = db.users.find_one({
            "email": email,
            "password": password
        })

        if user:
            session["_id"] = str(user["_id"])
            return True
        else:
            return False


    def getUserById(self, userId=0):
        try:
            user = db.users.find_one({
                "_id": ObjectId(userId)
            })

            return user

        except:
            return None


    def updateUser(self, user=None):
        try:
            db.users.update({
                "_id": ObjectId(user.id)
            }, {"$set": {
                "name": user.name,
                "email": user.email,
                "password": user.password
            }})

            return True
        except:
            return False

    def deleteUserById(self, userId=0):
        try:
            db.users.remove({
                "_id": ObjectId(userId)
            })

            return True
        except:
            return False
