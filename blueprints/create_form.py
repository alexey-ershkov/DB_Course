from flask import Blueprint, render_template, request, session, redirect
from utils import UseDb, sql_parser, create_role_config


def create_form_blueprint(root_config, routes, query_filename, inner_name):
    form_blueprint = Blueprint(inner_name, __name__, template_folder='templates')

    @form_blueprint.route(routes.get_url_by_inner_name(inner_name), methods=['GET', 'POST'])
    def get_docs():
        curr_role = session.get('role')
        if curr_role is None:
            return redirect('/login')
        if curr_role not in routes.get_access_config_by_inner_name(inner_name):
            return render_template('access_denied.html', routes=routes.get_routes_by_role(curr_role))
        routes.set_active(routes.get_url_by_inner_name(inner_name))
        if request.method == "POST":
            config = create_role_config(root_config)
            with UseDb(config) as db:
                r_form = request.form
                ans = db.execute(sql_parser(query_filename), r_form['year'], r_form['month'])
                return render_template('table.html', routes=routes.get_routes_by_role(curr_role), result=ans[0])
        else:
            return render_template('form.html', routes=routes.get_routes_by_role(curr_role))

    return form_blueprint
