from flask import request, render_template

from great import app
from great import db

from great.models.User import User
from great.models.Class import Class
from great.models.Invite import Invite
from great.models.Email import Email

@app.route("/classroom/classes/<class_id>/invites/", methods=["POST"])
def send_invite(class_id):
    email = request.form.get("email")
    createdAt = request.form.get("createdAt")

    user = User().getUserByEmail(email)
    classe = Class().getClassById(class_id)

    if user:
        invite = Invite(user=user, classe=classe, createdAt=createdAt, status="sent")
    else:
        invite = Invite(user={"email": email}, classe=classe, createdAt=createdAt, status="sent")

    invite_id = invite.createInvite(invite)
    title = "Convite Classroom"
    message = "Você foi convidado para participar da turma {0} no Classroom!<br><a href='http://200.137.131.118/classroom/invites/{1}/entry/'>Aceitar</a>".format(classe["name"], invite_id)

    e = Email().send(title="Convite Classroom", message=message, email=email)

    return "OK", 200


@app.route("/classroom/invites/<invite_id>/", methods=["DELETE"])
def delete_invite(invite_id):
    if Invite().deleteInviteById(invite_id):
        return "OK", 200
    else:
        return "Error", 400
