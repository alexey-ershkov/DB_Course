from flask import Blueprint, render_template, request, redirect, session
from utils import UseDb, sql_parser, create_role_config


def create_order_blueprint(root_config, routes):
    order_blueprint = Blueprint('order', __name__, template_folder='templates')

    @order_blueprint.route('/order', methods=['GET', 'POST'])
    def login_into():
        curr_role = session.get('role')
        if curr_role is None:
            return redirect('/login')
        name = session.get('name')
        surname = session.get('surname')
        manager_id = session.get('manager_id')
        if manager_id is None:
            routes.clear()
            return render_template('access_denied.html', routes=routes.get_routes_by_role(curr_role), name=name,
                                   surname=surname)
        config = create_role_config(root_config)
        with UseDb(config) as db:
            orders = db.execute(sql_parser('./SqlQueries/get_manager_orders.sql'), manager_id)[0]
            return render_template('order.html', name=name, surname=surname, orders=orders)

    return order_blueprint
