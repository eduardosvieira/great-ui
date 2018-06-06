from flask import request, render_template

from great import app
from great import db

from great.models.Class import Class

@app.route("/classroom/tasks/", methods=["POST"])
def create_task():
    title = request.form.get("title")
    description = request.form.get("description")
    deadline = request.form.get("deadline")
    classId = request.form.get("classId")
    classe = Class().getClassById(classId=classId)
    testId = request.form.get("testId")

    return "OK", 200
