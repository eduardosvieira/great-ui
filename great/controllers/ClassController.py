from flask import session, render_template, redirect, request

from app import app
from great.models.Class import Class
from great.models.User import User


@app.route("/classroom/", methods=["GET"])
def classroom_index():
    # Verifica se o usuário está logado, procurando pelo email dele na sessão
    if "_id" in session:
        # Pegue do banco de dados as turmas criadas pelo usuário
        classes = Class().getAllClassesByUserId(session["_id"])

        # Renderiza a página principal mostrando as classes do usuário logado
        return render_template("classroom.html", classes=classes)

    # Redireciona o usuário para página de login
    return redirect("/login/")

@app.route("/classroom/classes/", methods=["POST"])
def create_class():
    try:
        name = request.form.get("name")
        description = request.form.get("description")
        createdAt = request.form.get("createdAt")
        user = User().getUserById(session["_id"])

        classe = Class(name=name, description=description, user=user, createdAt=createdAt)

        classe.createClass(classe)

        return "OK", 200
    except:
        return "Error", 400


@app.route("/classroom/classes/<class_id>/", methods=["GET"])
def get_class(class_id):
    classe = Class().getClassById(class_id)

    return classe


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
