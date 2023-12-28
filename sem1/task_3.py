"""Написать функцию, которая будет принимать на вход два
числа и выводить на экран их сумму"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


# @app.route('/')
# def sum_(a=5, b=6):
#     c = a+b
#     return f'сумма {a}+{b} = {c}'

@app.route('/')
def index():
    context = {
        'a': 4,
        'b': 8,
    }
    context['c'] = context['a'] + context['b']
    return render_template('index.html', **context)


@app.route('/sum/<int:num1>/<int:num2>')
def sum_(num1, num2):
    res = num1 + num2
    return f'сумма {num1} и {num2} = {res}'


if __name__ == '__main__':
    app.run(debug=True)
