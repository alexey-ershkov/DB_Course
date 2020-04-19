from flask import Flask, render_template
from models import Database, Routes
from utils import sql_parser

app = Flask(__name__)
db = Database()
routes = Routes()


@app.route('/')
def main_page():
    routes.clear()
    return render_template('index.html', routes=routes.links)


@app.route('/1')
def first_query():
    routes.set_active('1')
    ans = db.execute(sql_parser('SqlQueries/1.sql'))
    return render_template('table.html', routes=routes.links, result=ans[0])


@app.route('/2')
def second_query():
    routes.set_active('2')
    ans = db.execute(sql_parser('SqlQueries/2.sql'))
    return render_template('table.html', routes=routes.links, result=ans[0])


@app.route('/3')
def third_query():
    routes.set_active('3')
    ans = db.execute(sql_parser('SqlQueries/3.sql'))
    return render_template('table.html', routes=routes.links, result=ans[0])


@app.route('/4')
def forth_query():
    routes.set_active('4')
    ans = db.execute(sql_parser('SqlQueries/4.sql'))
    return render_template('table.html', routes=routes.links, result=ans[0])


@app.route('/5')
def fifth_query():
    routes.set_active('5')
    ans = db.execute(sql_parser('SqlQueries/5.sql'))
    return render_template('table.html', routes=routes.links, result=ans[0])


@app.route('/6')
def sixth_query():
    routes.set_active('6')
    ans = db.execute(sql_parser('SqlQueries/6.sql'))
    return render_template('table.html', routes=routes.links, result=ans[0])


@app.route('/7')
def form():
    routes.set_active('7')
    return render_template('form.html', routes=routes.links)


if __name__ == '__main__':
    app.run()
