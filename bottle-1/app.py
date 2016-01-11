# -*- encoding: utf-8 -*-

from bottle import Bottle, run

app = Bottle()


@app.route('/')
def hello():
    return "Hello World!"


run(app, host='localhost', port=8080)
