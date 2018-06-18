from bson.objectid import ObjectId
from great import db

class Class():
    def __init__(self, id=0, name="", description="", creator=None, createdAt=""):
        self.id = id
        self.name = name
        self.description = description
        self.creator = creator
        self.createdAt = createdAt


    def createClass(self, classe=None):
        try:
            db.classes.insert({
                "name": classe.name,
                "description": classe.description,
                "createdAt": classe.createdAt,
                "creator": classe.creator
            })

            return True
        except:
            return False

    def getAllClassesByUserId(self, userId):
        try:
            classes = db.classes.find({
                "creator._id": ObjectId(userId)
            })

            return classes
        except:
            return None


    def getClassById(self, classId=""):
        try:
            c = db.classes.find_one({
                "_id": ObjectId(classId)
            })

            return c
        except:
            return None


    def updateClass(self, classe=None):
        try:
            db.classes.update({
                "_id": ObjectId(classe.id)
            }, {"$set": {
                "name": classe.name,
                "description": classe.description
            }})

            return True
        except:
            return False


    def deleteClassById(self, classId=0):
        try:
            db.classes.remove({
                "_id": ObjectId(classId)
            })

            return True
        except:
            return False
