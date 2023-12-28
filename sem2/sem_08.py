"""
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!"
"""
from flask import Flask, request, render_template, redirect, url_for, abort, flash

app = Flask(__name__)
app.secret_key = b'5c361513df1198a75cc1b14663281730904c3e4abf7defedd39f1cdf34af3000'


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        flash(f'Привет {name}!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(port=9000, debug=True)
