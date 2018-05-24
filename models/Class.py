from bson.objectid import ObjectId
from app import db

class Class():
    def __init__(self, id=0, name="", description="", user=None, createdAt=""):
        self.id = id
        self.name = name
        self.description = description
        self.user = user
        self.createdAt = createdAt


    def createClass(self, class=None):
        try:
            db.classes.insert({
                "name": class.name,
                "description": class.description,
                "createdAt": class.createdAt,
                "user": class.user
            })

            return True
        except:
            return False

    def getAllClassesByUserId(self, userId):
        try:
            classes = db.classes.find({
                "user._id": ObjectId(userId)
            })

            return classes
        except:
            return None


    def getClassById(self, classId):
        try:
            c = db.classes.find_one({
                "_id": ObjectId(classId)
            })

            return c
        except:
            return None
