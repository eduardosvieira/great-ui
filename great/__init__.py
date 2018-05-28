from flask import Flask, render_template, flash, redirect, url_for, session,logging
from great.data import *
from great.forms import *
from pymongo import MongoClient

app = Flask (__name__)

app.config["SECRET_KEY"] = "sjakjsaus8as9s997"

client = MongoClient('mongodb://localhost:27017/')
db = client.classroomdb


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('registrar.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/disciplinas')
def disciplinas():
    disciplinas = create_disciplinas()
    return render_template('disciplinas.html',disciplinas=disciplinas)

@app.route('/disciplina/<id>')
def disciplina(id):
    topicos = create_topicos()
    return render_template('disciplina.html',topicos=topicos)


@app.route('/turma/<id>')
def turma(id):
    turma = Turma(1,'FC - T02','FUNDAMENTO DE COMPUTAÇÃO','2017.2',33)
    participantes = create_participantes()
    tarefas = create_tarefas()
    return render_template('turma.html', turma=turma,participantes=participantes,tarefas=tarefas)


@app.route('/topicos')
def topicos():
    topicos =  create_topicos()
    return render_template('topicos.html', topicos=topicos)

@app.route('/authoring')
def authoring():
    return render_template('authoring.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/gamecenter')
def gamecenter():
    return render_template('gamecenter.html')

from great.controllers import ClassController
from great.controllers import UserController
