from flask import Flask, render_template, redirect, make_response, request
from flask_restful import abort, Api

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/document/<string:id>")
def document(id):
    return render_template(f"document{id}.html")


if __name__ == '__main__':
    app.run()
