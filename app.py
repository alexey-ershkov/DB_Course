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


@app.route('/first')
def first_query():
    routes.set_active('first')
    ans = db.execute(sql_parser('SqlQueries/first.sql'))
    print(ans)
    return render_template('first.html', routes=routes.links)


if __name__ == '__main__':
    app.run()
