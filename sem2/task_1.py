"""
Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('task_01.html')


@app.route('/submit/', methods=['POST'])
def submit():
    name = request.form.get('name')
    return f'Hello {name}!'


if __name__ == '__main__':
    app.run(debug=True, port=8000)
