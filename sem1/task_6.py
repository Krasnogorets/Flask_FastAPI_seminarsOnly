"""Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: "Имя",
"Фамилия", "Возраст", "Средний балл".
Данные о студентах должны быть переданы в шаблон через
контекст."""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/table/')
def table():
    _students = [{'name': 'иван',
                  'second_name': 'иванов',
                  'age': 18,
                  'avg_score': 3.8,
                  },
                 {'name': 'петр',
                  'second_name': 'петров',
                  'age': 20,
                  'avg_score': 4.8,
                  },
                 {'name': 'маша',
                  'second_name': 'машина',
                  'age': 21,
                  'avg_score': 4.0,
                  }]
    context = {'users': _students}
    return render_template('table.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
