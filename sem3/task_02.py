"""
Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
содержать следующие поля:
○ Имя пользователя (обязательное поле)
○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
заполнено или данные не прошли валидацию, то должно выводиться соответствующее
сообщение об ошибке.
Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
об ошибке.
"""

from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from flask import Flask, request, render_template, redirect, flash, url_for
from task_02_key import key
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from models_02 import db, Users

app = Flask(__name__)
app.config['SECRET_KEY'] = key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command("init-db1")
def init_db1():
    db.create_all()
    print('OK')


@app.route('/')
def index():
    return 'start'


@app.route('/success/')
def success():
    return 'вы успешно зарегистрированны'


@app.route('/error/')
def error():
    return 'такое имя уже существует'


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password_conf = PasswordField('password_conf', validators=[DataRequired(), EqualTo('password'), Length(min=6)])


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        pass
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        if Users.query.filter(Users.username == form.username.data).first():
            flash('такой пользователь существует!', 'danger')
            return redirect(url_for('register'))
        else:
            user = Users(username=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Форма успешно отправлена!', 'success')
            return redirect(url_for('register'))

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
