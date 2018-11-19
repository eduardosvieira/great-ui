from flask import jsonify, request, render_template, redirect, session
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

from great import app
from great import db


#Retornando todas os usuários no BD
@app.route("/quiz/users/", methods=["GET"])
def get_all_users():
    result = db.users.find()

    users = []
    for item in result:
        if item["_id"]:
            item["_id"] = str(item["_id"])
        users.append(item)

    return jsonify(users)

#Logout do sistema
@app.route("/quiz/logout/", methods=["GET"])
def qlogout():
    session.pop("email", None)
    return redirect("/quiz/login/")
