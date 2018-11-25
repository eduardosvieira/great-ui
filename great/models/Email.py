from flask import request, session, render_template, jsonify, redirect

from bson.objectid import ObjectId

from great import app
from great import db

from flask_mail import Message

from great import mail

class Email():
  def send(self, title="", message="", email=""):
    msg = Message(
      title,
      sender='lawsclassroom@gmail.com',
      recipients=[email])

    msg.html = message
    mail.send(msg)
