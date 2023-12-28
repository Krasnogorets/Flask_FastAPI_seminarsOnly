from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    # return 'Hello World'
    return f'число {42}'


if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
