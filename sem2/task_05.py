"""
Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом.
"""
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('task_05.html')


@app.post('/submit')
def submit():
    num1 = int(request.form['number_1'])
    num2 = int(request.form['number_2'])
    operation = request.form['operation']
    print(operation)
    match operation:
        case "add":
            text = f'{num1} + {num2} = {num1 + num2}'
        case "sub":
            text = f'{num1} - {num2} = {num1 - num2}'
        case "mul":
            text = f'{num1} * {num2} = {num1 * num2}'
        case "div":
            text = f'{num1} : {num2} = {num1 / num2}'
    return redirect(url_for('result', text=str(text)))


@app.route('/result/<text>')
def result(text):
    return render_template('result1.html', text=text)


if __name__ == '__main__':
    app.run(port=9000, debug=True)
