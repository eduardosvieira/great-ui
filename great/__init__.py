from flask import Flask, render_template, flash, redirect, url_for, session,logging

from pymongo import MongoClient
from flask_mail import Mail
from flask_gravatar import Gravatar


app = Flask (__name__)

app.config.update(
        DEBUG=True,
        #EMAIL SETTINGS
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME = 'lawsclassroom@gmail.com',
        MAIL_PASSWORD = '@lawsclassroom'
        )

mail=Mail(app)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    use_ssl=False,
                    base_url=None)


app.config["SECRET_KEY"] = "sjakjs45454s@#4s8as9s997"

client = MongoClient("mongodb://eduardo:secretPassword@200.137.131.118/classroomdb")
db = client.classroomdb

print(db.users.count())

from great.controllers import DefaultController
from great.controllers import ClassController
from great.controllers import UserController
from great.controllers import TaskController
from great.controllers import NoticeController
from great.controllers import InviteController

from great.controllers.quiz import routes, CourseController, QuestionController, TopicController, UserController, TestController, AnswerController, ClassController
