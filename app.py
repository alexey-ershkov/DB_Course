from flask import Flask, render_template, request, redirect
from utils import Routes
import blueprints
import json

app = Flask(__name__)
app.url_map.strict_slashes = False
routes = Routes()


@app.before_request
def clear_trailing():
    request_path = request.path
    if request_path != '/' and request_path.endswith('/'):
        return redirect(request_path[:-1])


with open("dataFiles/db_connect.json", "r") as config_file:
    app.config['db_config'] = json.load(config_file)

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
    return render_template('index.html', routes=routes.get_routes)


if __name__ == '__main__':
    app.run()
