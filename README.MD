1 - Instalar o virtualenv
$ pip install virtualenv

2 - Inicial o virtual env
$ virtualenv -p python3 venv

3 - Ativar o ambiente virtual
$ . venv/bin/activate

4 - Rodar a app
$ python3 run.py runserver


4 - Para ver tudo o que tá instalado no ambiente virtual
$ pip3 freeze


5 - Para instalar tudo duma vez
$ pip install -r requirements.txt


6 - Organizar as pastas

app
- controllers
-- __init__.py
- models
-- __init__.py
- static
- templates
run.py



7 - Usar o ORM SQL-Alchemy

8 - Criar as classes no arquivo models/tables.py

9 - Script e Migrate
$ pip3 install flask-script
$ pip3 install flask-migrate

9 - Iniciar o banco de dados

$ python3 run.py db init
