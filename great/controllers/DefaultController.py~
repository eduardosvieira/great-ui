from flask import session, render_template, redirect

from app import app
from great.models.Class import Class

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/authoring/')
def authoring():
    return render_template('authoring.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/gamecenter')
def gamecenter():
    return render_template('gamecenter.html')

@app.route("/classroom/", methods=["GET"])
def classroom_index():
    # Verifica se o usuário está logado, procurando pelo email dele na sessão
    if "_id" in session:
        # Pegue do banco de dados as turmas criadas pelo usuário
        classes = Class().getAllClassesByUserId(session["_id"])

        # Renderiza a página principal mostrando as classes do usuário logado
        return render_template("classroom.html", classes=classes)

    # Redireciona o usuário para página de login
    return redirect("/login/")
