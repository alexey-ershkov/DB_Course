from flask import Flask, render_template, request
from models import Database, Routes
from utils import sql_parser

app = Flask(__name__)
routes = Routes()


@app.route('/')
def main_page():
    routes.clear()
    return render_template('index.html', routes=routes.links)


@app.route('/1')
def first_query():
    db = Database()
    routes.set_active('1')
    ans = db.execute(sql_parser('SqlQueries/1.sql'))
    del db
    return render_template('table.html', routes=routes.links, result=ans[0])


@app.route('/2')
def second_query():
    db = Database()
    routes.set_active('2')
    ans = db.execute(sql_parser('SqlQueries/2.sql'))
    del db
    return render_template('table.html', routes=routes.links, result=ans[0])


@app.route('/3')
def third_query():
    db = Database()
    routes.set_active('3')
    ans = db.execute(sql_parser('SqlQueries/3.sql'))
    del db
    return render_template('table.html', routes=routes.links, result=ans[0])


@app.route('/4')
def forth_query():
    db = Database()
    routes.set_active('4')
    ans = db.execute(sql_parser('SqlQueries/4.sql'))
    del db
    return render_template('table.html', routes=routes.links, result=ans[0])


@app.route('/5')
def fifth_query():
    db = Database()
    routes.set_active('5')
    ans = db.execute(sql_parser('SqlQueries/5.sql'))
    del db
    return render_template('table.html', routes=routes.links, result=ans[0])


@app.route('/6')
def sixth_query():
    db = Database()
    routes.set_active('6')
    ans = db.execute(sql_parser('SqlQueries/6.sql'))
    del db
    return render_template('table.html', routes=routes.links, result=ans[0])


@app.route('/7', methods=['GET', 'POST'])
def form():
    routes.set_active('7')
    if request.method == "POST":
        db = Database()
        r_form = request.form
        ans = db.execute(sql_parser('SqlQueries/7.sql'), r_form['year'], r_form['month'])
        del db
        return render_template('message.html', routes=routes.links, result=ans[0])
    else:
        return render_template('form.html', routes=routes.links)


@app.route('/8', methods=['GET', 'POST'])
def get_docs():
    routes.set_active('8')
    if request.method == "POST":
        db = Database()
        r_form = request.form
        ans = db.execute(sql_parser('SqlQueries/8.sql'), r_form['month'], r_form['year'])
        del db
        return render_template('table.html', routes=routes.links, result=ans[0])
    else:
        return render_template('form.html', routes=routes.links)


if __name__ == '__main__':
    app.run()
