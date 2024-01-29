"""
Создать базу данных для хранения информации о студентах университета.
База данных должна содержать две таблицы: "Студенты" и "Факультеты".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
В таблице "Факультеты" должны быть следующие поля: id и название факультета.
Необходимо создать связь между таблицами "Студенты" и "Факультеты".
Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.
"""
import random
from flask import Flask, request, render_template, redirect, url_for
from models_01 import db, Students, Facultie, Rate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db.init_app(app)


@app.route('/')
def index():
    return 'start'


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_tables():
    count = 5
    faculties = []
    gender = ['male', 'femail']
    for i in range(1, count + 1):
        new_facultie = Facultie(name=f'Facultie{i}')
        faculties.append(new_facultie)
        db.session.add(new_facultie)
    db.session.commit()
    students = []
    for i in range(1, count + 1):
        new_student = Students(name=f'Ivan_{i}',
                               second_name=f'Ivanov_{i}', third_name=f'Ivanovich', email=f'Ivan_{i}@mail.ru',
                               age=21, gender=random.choice(gender),
                               group=f'group_{i}'
                               , facultie_id=i)

        #
        students.append(new_student)
        db.session.add(new_student)

    db.session.commit()
    print(students)
    print('OK')


@app.cli.command("fill-rates")
def fill_rates():
    marks = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(1, 6):
        rate = Rate(subject='математика', mark=random.choice(marks), student_id=i)
        db.session.add(rate)
    db.session.commit()


@app.cli.command("del")
def del_user():
    user = Rate.query.filter_by(student_id=1).first()
    db.session.delete(user)
    user = Rate.query.filter_by(student_id=2).first()
    db.session.delete(user)
    user = Rate.query.filter_by(student_id=3).first()
    db.session.delete(user)
    user = Rate.query.filter_by(student_id=4).first()
    db.session.delete(user)
    user = Rate.query.filter_by(student_id=5).first()
    db.session.delete(user)
    db.session.commit()
    print('Delete from DB!')


@app.route('/students/')
def all_students():
    students = Students.query.all()
    print(students)
    context = {'students': students}
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
