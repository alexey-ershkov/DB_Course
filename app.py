from flask import Flask, render_template
import models

app = Flask(__name__)


@app.route('/')
def main_page():
    routes = models.index_model()
    return render_template('index.html', routes=routes)


if __name__ == '__main__':
    app.run()
