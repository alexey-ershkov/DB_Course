from flask import session, redirect
from utils import UseDb, sql_parser


def create_role_config(root_config):
    with UseDb(root_config) as db:
        role_config = {'host': root_config['host'], 'db': root_config['db']}
        cookie_role = session.get('role')
        if not cookie_role:
            redirect('/login')
        role = db.execute(sql_parser('./SqlQueries/get_role_info.sql'), cookie_role)[0]
        role_config['user'] = role[0]['login']
        role_config['password'] = role[0]['password']

        return role_config
