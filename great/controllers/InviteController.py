from flask import request, render_template

from great import app
from great import db

from great.models.Class import Class
from great.models.Notice import Notice


@app.route("/classroom/classes/<class_id>/invites/", methods=["POST"])
def send_invite(class_id):
    email = request.form.get("email")

    print("Convite enviado para " + email)

    return "OK", 200
