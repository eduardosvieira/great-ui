
from flask import request, session, render_template, jsonify, redirect

from flask_mail import Message
from app import mail

class Email():
    def __init__(self):
        pass

    def send(self, title="", message="", email=""):
        msg = Message(
            title,
            sender='edusvieirap@gmail.com',
            recipients=
            [email])

        msg.html = message
        mail.send(msg)

        return True
