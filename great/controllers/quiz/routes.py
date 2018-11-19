from flask import render_template, request, redirect, session


from great import app
from great import db


#Redirecionando para o índice da aplicação
@app.route("/quiz/", methods=["GET"])
def qindex():
    if "email" in session:
        created_tests = db.tests.find(
                        {
                            "creator.email" : session["email"]
                        })
        tests = db.tests.find(
                {
                    "people" : session["email"]
                })

        return render_template("quiz/index.html", created_tests=created_tests, tests=tests)

    return redirect("/login/")

#Redirecionando para dashboard
@app.route("/quiz/dashboard/", methods=["GET"])
def qdashboard():
    return render_template("quiz/dashboard/index.html")
