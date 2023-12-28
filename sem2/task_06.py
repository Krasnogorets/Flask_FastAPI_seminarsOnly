"""
Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.
"""
from flask import Flask, request, render_template, redirect, url_for, abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('task_06.html')


@app.post('/submit')
def submit():
    age = int(request.form['age'])
    if age > 18:
        return redirect(url_for('result', age=age))
    abort(404)


@app.route('/result/<age>')
def result(age):
    return render_template('result2.html', age=age)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(port=9000, debug=True)
