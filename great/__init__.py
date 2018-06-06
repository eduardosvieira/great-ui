from flask import Flask, render_template, flash, redirect, url_for, session,logging
from great.data import *
from great.forms import *
from pymongo import MongoClient

app = Flask (__name__)

app.config["SECRET_KEY"] = "sjakjs45454s@#4s8as9s997"

client = MongoClient('mongodb://localhost:27017/')
db = client.classroomdb

from great.controllers import DefaultController
from great.controllers import ClassController
from great.controllers import UserController
from great.controllers import TaskController
