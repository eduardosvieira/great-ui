from flask import request, render_template

from great import app
from great import db

from great.models.Class import Class
from great.models.Task import Task

@app.route("/classroom/tasks/", methods=["POST"])
def create_task():
    title = request.form.get("title")
    description = request.form.get("description")
    createdAt = request.form.get("createdAt")
    deadline = request.form.get("deadline")
    classId = request.form.get("classId")
    classe = Class().getClassById(classId=classId)
    testId = request.form.get("testId")
    test = ""

    task = Task(title=title, description=description, createdAt=createdAt, deadline=deadline, classe=classe, test=test)

    if Task().createTask(task):
        return "OK", 200

    else:
        return "Error", 400
