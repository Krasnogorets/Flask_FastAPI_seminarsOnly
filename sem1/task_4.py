"""Написать функцию, которая будет принимать на вход строку и
выводить на экран ее длину.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/str/<path:stroka>/')
def index(stroka):
    res = len(str(stroka).replace('/', ''))
    return f'длина строки {stroka} без слешей равна = {res}'


if __name__ == '__main__':
    app.run(debug=True)
