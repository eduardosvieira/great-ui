from flask import request, render_template

from great import app
from great import db

from great.models.User import User
from great.models.Class import Class
from great.models.Invite import Invite


@app.route("/classroom/classes/<class_id>/invites/", methods=["POST"])
def send_invite(class_id):
    email = request.form.get("email")
    createdAt = request.form.get("createdAt")

    user = User().getUserByEmail(email)
    classe = Class().getClassById(class_id)

    invite = Invite(user=user, classe=classe, createdAt=createdAt, status="sent")

    if invite.createInvite(invite):
        return "OK", 200
    else:
        return "Error", 400
