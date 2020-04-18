from flask import Flask, render_template
from Database import Database

routes = [
    {'name': 'Составить отчет о банкетах в марте 2017 года', 'href': 'first', 'active': False},
    {'name': 'Составить отчет о работе менеджеров в марте 2017', 'href': 'second', 'active': False},
    {'name': 'Показать все сведения о самом молодом менеджере', 'href': 'third', 'active': False},
    {'name': 'Показать сведения о менеджерах, которые пока не обслуживали ни один банкет, которые не приняли ни '
             'одного заказа', 'href': 'forth', 'active': False},
    {'name': 'Показать сведения о менеджерах, не принявших ни одного заказа в марте 2013 года', 'href': 'fifth',
     'active': False},
    {'name': 'Показать сведения о зале, который чаще всех заказывали в 2017', 'href': 'sixth', 'active': False},
]

app = Flask(__name__)
db = Database()


@app.route('/')
def main_page():
    res = db.first()
    print(res)
    return render_template('index.html', routes=routes)


if __name__ == '__main__':
    app.run()
