from flask import request, render_template

from great import app
from great import db

from great.models.Class import Class
from great.models.Notice import Notice

@app.route("/classroom/notices/", methods=["POST"])
def create_notice():
    title = request.form.get("title")
    description = request.form.get("description")
    createdAt = request.form.get("createdAt")
    classId = request.form.get("classId")
    classe = Class().getClassById(classId=classId)

    notice = Notice(title=title, description=description, createdAt=createdAt, classe=classe)

    if Notice().createNotice(notice):
        return "OK", 200

    else:
        return "Error", 400
