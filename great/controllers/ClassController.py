from flask import session, render_template, redirect, request

from app import app
from great.models.Class import Class
from great.models.User import User

@app.route("/classroom/classes/", methods=["POST"])
def create_class():
    try:
        name = request.form.get("name")
        description = request.form.get("description")
        createdAt = request.form.get("createdAt")
        creator = User().getUserById(session["_id"])

        classe = Class(name=name, description=description, creator=creator, createdAt=createdAt)

        classe.createClass(classe)

        return "OK", 200
    except:
        return "Error", 400


@app.route("/classroom/classes/<class_id>/", methods=["GET"])
def get_class(class_id):
    classe = Class().getClassById(class_id)

    return render_template("turma.html", classe=classe)


@app.route("/classroom/classes/<class_id>/", methods=["PUT"])
def update_class(class_id):
    name = request.form.get("name")
    description = request.form.get("description")

    classe = Class(name=name, description=description)

    classe.updateClass(classe)

    return "OK", 200


@app.route("/classroom/classes/<class_id>/", methods=["DELETE"])
def delete_class(class_id):
    Class().deleteClassById(class_id)

    return "OK", 200
