"""
Создать базовый шаблон для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон.
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/main/')
def main():
    context = {'title': 'Главная',
               'content': "главная странгица учебного проекта"}
    return render_template('main.html', **context)


@app.route('/about/')
def about():
    context = {'title': 'О нас',
               'content': "мы самые лучшие программисты"}
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {'title': 'Контакты',
               'content': "тел 458588558, почта, лвллвдвдвд"}
    return render_template('contacts.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
