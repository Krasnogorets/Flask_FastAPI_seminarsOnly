"""
Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.
"""
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('task_04.html')


@app.post('/submit')
def submit():
    text = request.form['text']
    return redirect(url_for('result', lenght=len(text.split())))


@app.route('/result/<lenght>')
def result(lenght):
    return render_template('result.html', lenght=lenght)


if __name__ == '__main__':
    app.run(port=9000, debug=True)
