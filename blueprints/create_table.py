from flask import Blueprint, render_template, session, redirect
from utils import UseDb, sql_parser, create_role_config


def create_table_blueprint(root_config, routes, query_filename, inner_name):
    table_blueprint = Blueprint(inner_name, __name__, template_folder='templates')

    @table_blueprint.route(routes.get_url_by_inner_name(inner_name))
    def table_query():
        curr_role = session.get('role')
        if curr_role is None:
            return redirect('/login')
        if curr_role not in routes.get_access_config_by_inner_name(inner_name):
            return render_template('access_denied.html', routes=routes.get_routes_by_role(curr_role))
        config = create_role_config(root_config)
        with UseDb(config) as db:
            routes.set_active(routes.get_url_by_inner_name(inner_name))
            ans = db.execute(sql_parser(query_filename))
            return render_template('table.html', routes=routes.get_routes_by_role(curr_role), result=ans[0])

    return table_blueprint
