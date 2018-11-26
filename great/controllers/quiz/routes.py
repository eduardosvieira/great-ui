#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import session, render_template, redirect

from bson.objectid import ObjectId

from great import app
from great import db

@app.route("/quiz/", methods=["GET"])
def index_quiz():

    # Verifica se o usuário está logado, procurando pelo email dele na sessão
    if "email" in session:

        # Requisita do banco os quizes criados pelo usuário
        quizzes = db.tests.find(
                        {
                            "creator._id" : ObjectId(session["_id"])
                        })

        # Renderiza a página mostrando os quizes do usuário logado
        return render_template("quiz/index.html", quizzes=quizzes)

    # Redireciona o usuário para página de login
    return redirect("/login/")
