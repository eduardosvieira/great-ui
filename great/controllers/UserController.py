from flask import session, render_template, redirect, request

from app import app
from great.models.User import User

@app.route("/login/", methods=["GET"])
def login_index():
    if "_id" in session:
        return redirect("/classroom/")
    else:
        return render_template("login/login.html")


@app.route("/login/", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    print(password)

    print(User().loginUser(email=email, password=password))

    if User().loginUser(email=email, password=password):
        print("oi")
        return redirect("/classroom/")
    else:
        return render_template("login/login.html", error="Usuário ou senha estão incorretos!")
