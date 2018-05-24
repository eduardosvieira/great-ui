from bson.objectid import ObjectId
from app import db

class Class():
    def __init__(self, id=0, name="", description="", user=None, createdAt=""):
        self.id = id
        self.name = name
        self.description = description
        self.user = user
        self.createdAt = createdAt
