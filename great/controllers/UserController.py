from flask import session, render_template, redirect, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from great import app
from great.models.User import User

@app.route("/login/", methods=["GET"])
def login_index():
    if "_id" in session:
        return redirect("/classroom/")
    else:
        return render_template("user/login.html")


@app.route("/login/", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    password = generate_password_hash(request.form.get("password"))
    user = User().getUserByEmail(email)

    if user:
        if check_password_hash(user["password"], password):
            session["email"] = user["email"]
            session["name"] = user["name"]
            session["_id"] = str(user["_id"])
            return redirect("/classroom/")

    error = "E-mail ou senha estão incorretos!"
    return render_template("user/login.html", error=error)

@app.route('/logout/')
def logout():
    if '_id' in session:
        session.pop('_id')
    return redirect(url_for('index'))

#Redirecionando usuário para a página de register
@app.route("/register/", methods=["GET"])
def redirect_register():
    return render_template("user/register.html")

@app.route("/register/", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    confirmar_password = request.form.get("confirmar_password")

    #Verificar se o usuario já existe
    user = User().getUserByEmail(email)

    if user:
        return render_template("user/register.html", error="E-mail já está sendo usado por outro usuário!")
    else:
        password = generate_password_hash(password)
        user = User(name=name, email=email, password=password)

        if User().signUpUser(user):
            return "OK", 200

        else:
            return "Error", 400

        #return redirect("/classroom/")
