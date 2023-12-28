"""
Создать страницу, на которой будет форма для ввода логина
и пароля
При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.

"""
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

LOGIN = 'filipp'
PASS = '1234'


@app.route('/')
def index():
    return render_template('task_03.html')


@app.post('/submit')
def submit():
    username = request.form['login']
    if username == LOGIN and request.form['password'] == PASS:
        return redirect(url_for('sucsess', username=username))
    else:
        return redirect(url_for('stop'))


@app.route('/sucsess/<username>')
def sucsess(username):
    return render_template('sucsess.html', username=username)


@app.route('/stop')
def stop():
    return render_template('stop.html')


if __name__ == '__main__':
    app.run(port=9000, debug=True)
