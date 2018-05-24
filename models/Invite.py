from bson.objectid import ObjectId
from app import db

class Invite():
    def __init__(self, id=0, user=None, class=None, createdAt="", status=""):
        self.id = id
        self.user = user
        self.class = class
        self.createdAt = createdAt
        self.status = status

    def createInvite(self, invite=None):
        try:
            db.invites.insert({
                "user": invite.user,
                "class": invite.class,
                "createdAt": invite.createdAt,
                "status": invite.status
            })

            return True
        except:
            return False
