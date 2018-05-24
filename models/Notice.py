from bson.objectid import ObjectId
from app import db

class Notice():
    def __init__(self, id=0, title="", description="", class=None, createdAt=""):
        self.id = id
        self.title = title
        self.description = description
        self.class = class
        self.createdAt = createdAt


    def createNotice(self, notice=None):
        try:
            db.notices.insert({
                "title": notice.title,
                "description": notice.description,
                "class": notice.class,
                "createdAt": invite.createdAt
            })

            return True
        except:
            return False


    def getAllNoticesByClassId(self, classId):
        try:
            notices = db.notices.find({
                "class._id": ObjectId(classId)
            })

            return notices
        except:
            return None


    def getNoticeById(self, noticeId):
        try:
            notice = db.notices.find_one({
                "_id": ObjectId(noticeId)
            })

            return notice
        except:
            return None
