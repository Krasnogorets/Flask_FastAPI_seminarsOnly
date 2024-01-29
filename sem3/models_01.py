from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

"""
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
"""

db = SQLAlchemy()


class Facultie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=False, nullable=True)
    students = db.relationship('Students', backref=db.backref('facultie'), lazy=True)

    def __repr__(self):
        return f'Факультет: {self.name}'


class Rate(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String(80), nullable=True)
    mark = db.Column(db.Integer, unique=False, nullable=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=True)

    def __repr__(self):
        return f'предмет: {self.subject}, оценка: {self.mark}'


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=False, nullable=True)
    second_name = db.Column(db.String(120), unique=False, nullable=True)
    third_name = db.Column(db.String(120), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=True)
    gender = db.Column(db.String(10), unique=False, nullable=True)
    group = db.Column(db.String(10), unique=False, nullable=True)
    facultie_id = db.Column(db.Integer, db.ForeignKey('facultie.id'))
    created_at = db.Column(db.DateTime, default=datetime.now)
    rates = db.relationship('Rate', backref=db.backref('st_id'), lazy=True)

    def __repr__(self):
        return f'Студент: ({self.second_name}, {self.name}, {self.third_name}, {self.age}, {self.gender},' \
               f' {self.group},{self.email}, {self.facultie}, {self.rates})'
