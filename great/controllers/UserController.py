from flask import session, render_template, redirect

from app import app
from great.models.User import User

@app.route("/login/", methods=["GET"])
def login_index():
    if "_id" in session:
        return redirect("/classroom/")
    else:
        return render_template("login/login.html")
