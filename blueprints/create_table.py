from flask import Blueprint, render_template
from utils import UseDb, sql_parser


def create_table_blueprint(config, routes, query_filename, inner_name):
    table_blueprint = Blueprint(inner_name, __name__, template_folder='templates')

    @table_blueprint.route(routes.get_url_by_inner_name(inner_name))
    def table_query():
        with UseDb(config) as db:
            routes.set_active(routes.get_url_by_inner_name(inner_name))
            ans = db.execute(sql_parser(query_filename))
            return render_template('table.html', routes=routes.get_routes, result=ans[0])

    return table_blueprint
