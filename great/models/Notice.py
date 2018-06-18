from bson.objectid import ObjectId
from great import db

class Notice():
    def __init__(self, id=0, title="", description="", classe=None, createdAt=""):
        self.id = id
        self.title = title
        self.description = description
        self.classe = classe
        self.createdAt = createdAt


    def createNotice(self, notice=None):
        try:
            db.notices.insert({
                "title": notice.title,
                "description": notice.description,
                "class": notice.classe,
                "createdAt": notice.createdAt
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


    def updateNotice(self, notice=None):
        try:
            db.notices.update({
                "_id": ObjectId(notice.id)
            }, {"$set": {
                "title": notice.title,
                "description": notice.description
            }})

            return True
        except:
            return False

    def deleteNoticeById(self, noticeId=0):
        try:
            db.notices.remove({
                "_id": ObjectId(noticeId)
            })

            return True
        except:
            return False
