from flask import Blueprint, render_template, request, redirect, session
from utils import UseDb, sql_parser


def create_login_blueprint(app):
    login_blueprint = Blueprint('login', __name__, template_folder='templates')

    @login_blueprint.route('/login', methods=['GET', 'POST'])
    def login_into():
        if request.method == "POST":
            root_config = app.config['db_config']
            with UseDb(root_config) as db:
                login = request.form["login"]
                password = request.form["password"]
                user = db.execute(sql_parser('./SqlQueries/get_user_info.sql'), login)[0]
                if len(user) == 0 or user[0]["password"] != password:
                    return render_template('login_form.html')
                session['role'] = user[0]['role']
                return redirect('/')
        else:
            return render_template('login_form.html')

    return login_blueprint
