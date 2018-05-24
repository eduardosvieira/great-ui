from bson.objectid import ObjectId
from app import db

class Notice():
    def __init__(self, id=0, title="", description="", class=None, createdAt=""):
        self.id = id
        self.title = title
        self.description = description
        self.class = class
        self.createdAt = createdAt
