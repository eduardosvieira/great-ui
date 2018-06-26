from bson.objectid import ObjectId
from great import db

class Invite():
    def __init__(self, id=0, user=None, classe=None, createdAt="", status=""):
        self.id = id
        self.user = user
        self.classe = classe
        self.createdAt = createdAt
        self.status = status

    def createInvite(self, invite=None):
        try:
            id = db.invites.insert_one({
                "user": invite.user,
                "class": invite.classe,
                "createdAt": invite.createdAt,
                "status": invite.status
            }).inserted_id

            return id
        except:
            return None


    def getAllInvitesByClassId(self, classId):
        try:
            invites = db.invites.find({
                "class._id": ObjectId(classId)
            })

            return invites
        except:
            return None


    def getInviteById(self, inviteId):
        try:
            invite = db.invites.find_one({
                "_id": ObjectId(inviteId)
            })

            return invite
        except:
            return None


    def deleteInviteById(self, inviteId=0):
        try:
            db.invites.remove({
                "_id": ObjectId(inviteId)
            })

            return True
        except:
            return False
