from great import db

class Task():
    def __init__(self, id=0, title="", description="", classe=None, test=None, createdAt="", deadline=""):
        self.id = id
        self.title = title
        self.description = description
        self.classe = classe
        self.createdAt = createdAt
        self.deadline = deadline
        self.test = test

    def createTask(self, task):
        try:
            db.tasks.insert({
                "title": task.title,
                "description": task.description,
                "createdAt": task.createdAt,
                "class": task.classe,
                "deadline": task.deadline,
                "test": task.test
            })

            return True
        except:
            return False
