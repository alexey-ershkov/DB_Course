import datetime

from flask import Flask, render_template, request, redirect, session, url_for
from utils import Routes, create_role_config
import blueprints
import json
import uuid

app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = str(uuid.uuid1().hex)
app.permanent_session_lifetime = datetime.timedelta(days=1)

routes = Routes()


@app.before_request
def clear_trailing():
    request_path = request.path
    if request_path != '/' and request_path.endswith('/'):
        return redirect(request_path[:-1])


with open("dataFiles/db_connect.json", "r") as config_file:
    app.config['db_config'] = json.load(config_file)

app.register_blueprint(blueprints.create_login_blueprint(app))
app.register_blueprint(blueprints.create_logout_blueprint())
app.register_blueprint(blueprints.create_order_blueprint(app.config['db_config'], routes))

for route_info in routes.get_routes:
    if route_info['type'] == 'table':
        app.register_blueprint(blueprints.create_table_blueprint(
            app.config['db_config'],
            routes,
            route_info['queryFilename'],
            route_info['innerName']
        ))
    if route_info['type'] == 'form':
        app.register_blueprint(blueprints.create_form_blueprint(
            app.config['db_config'],
            routes,
            route_info['queryFilename'],
            route_info['innerName']
        ))


@app.route('/')
def main_page():
    routes.clear()
    curr_role = session.get('role')
    name = session.get('name')
    surname = session.get('surname')
    if curr_role is None:
        return redirect('/login')
    return render_template('index.html', routes=routes.get_routes_by_role(curr_role), name=name, surname=surname)


if __name__ == '__main__':
    app.run()
