from flask import Blueprint, render_template, request
from utils import UseDb, sql_parser


def create_form_blueprint(config, routes, query_filename, inner_name):
    form_blueprint = Blueprint(inner_name, __name__, template_folder='templates')

    @form_blueprint.route(routes.get_url_by_inner_name(inner_name), methods=['GET', 'POST'])
    def get_docs():
        routes.set_active(routes.get_url_by_inner_name(inner_name))
        if request.method == "POST":
            with UseDb(config) as db:
                r_form = request.form
                ans = db.execute(sql_parser(query_filename), r_form['year'], r_form['month'])
                return render_template('table.html', routes=routes.get_routes, result=ans[0])
        else:
            return render_template('form.html', routes=routes.get_routes)

    return form_blueprint
