from flask import Blueprint, render_template, request, redirect, session
from utils import UseDb, sql_parser, create_role_config


def create_order_blueprint(root_config, routes):
    order_blueprint = Blueprint('order', __name__, template_folder='templates')

    @order_blueprint.route('/order', methods=['GET', 'POST'])
    def orders_info():
        routes.clear()
        curr_role = session.get('role')
        if curr_role is None:
            return redirect('/login')
        name = session.get('name')
        surname = session.get('surname')
        manager_id = session.get('manager_id')
        if manager_id is None:
            return render_template('access_denied.html', routes=routes.get_routes_by_role(curr_role), name=name,
                                   surname=surname)
        config = create_role_config(root_config)
        with UseDb(config) as db:
            if request.method == "POST":
                r_form = request.form
                if r_form['type'] == 'add':
                    order_id = r_form['order_id']
                    dish_id = r_form['dish_id']
                    buf = session.get('order_info')
                    if buf is None:
                        buf = {}
                    info = buf.get(order_id)
                    if info is None:
                        buf[order_id] = {}
                    dish = buf[order_id].get(dish_id)
                    if dish is None:
                        buf[order_id][dish_id] = {'count': int(r_form['count']), 'name': r_form['name']}
                    else:
                        buf[order_id][dish_id]['count'] += int(r_form['count'])
                    session['order_info'] = buf
                else:
                    order_id = r_form['order_id']
                    upd_info = list(session.get('order_info').get(order_id).items())
                    buf = session['order_info']
                    buf.pop(order_id)
                    session['order_info'] = buf
                    for dish_id, dish_info in upd_info:
                        db.execute(sql_parser('./SqlQueries/insert_dish.sql'), order_id, dish_id,
                                   str(dish_info.get('count')))
                return redirect(request.url)
            else:
                order_id = request.args.get('id')
                if order_id is None:
                    orders = db.execute(sql_parser('./SqlQueries/get_manager_orders.sql'), manager_id)[0]
                    return render_template('manager_orders.html', name=name, surname=surname, orders=orders)
                else:
                    order_header_info = db.execute(sql_parser('./SqlQueries/get_order_header_info.sql'), manager_id,
                                                   order_id)[0][0]
                    if len(order_header_info) == 0:
                        return render_template('access_denied.html', routes=routes.get_routes_by_role(curr_role),
                                               name=name,
                                               surname=surname)
                    order_info = db.execute(sql_parser('./SqlQueries/get_order_info.sql'), order_id)[0]
                    menu = db.execute(sql_parser('./SqlQueries/get_menu.sql'))[0]
                    pre_ordered = session.get('order_info')
                    if pre_ordered is not None:
                        pre_ordered = pre_ordered.get(str(order_id))
                    if pre_ordered is not None:
                        pre_ordered = list(pre_ordered.values())
                    return render_template('order.html',
                                           name=name,
                                           surname=surname,
                                           header=order_header_info,
                                           menu=menu,
                                           ordered=order_info,
                                           pre_ordered=pre_ordered)

    return order_blueprint
