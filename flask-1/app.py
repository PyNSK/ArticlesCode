# -*- encoding: utf-8 -*-
import datetime
import json
import pickle

from flask import Flask, request
from flask import render_template

app = Flask(__name__)

PATH = 'store.pkl'
DATA = []


def read():
    global DATA
    try:
        with open(PATH, 'rb') as fio:
            DATA = pickle.load(fio)
    except FileNotFoundError:
        DATA = []


def write(value):
    global DATA
    DATA.append(value)
    with open(PATH, 'wb') as fio:
        pickle.dump(DATA, fio)


@app.route("/")
def index():
    global DATA
    return render_template("index.html", data=json.dumps(DATA))


@app.route('/save')
def save():
    result = 'Error'
    val = request.args.get('value')
    if val is not None:
        result = 'OK'
        write([int(datetime.datetime.now().timestamp() * 1000), int(val)])
    return result


if __name__ == "__main__":
    read()
    app.run(debug=True)
