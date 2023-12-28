from flask import Flask

app = Flask(__name__)


#
# @app.route('/')
# def hello():
#     return 'Hello, World!'


@app.route('/about/')
def about():
    return f'page about'


@app.route('/contact/')
def contact():
    return f'page contact'


if __name__ == '__main__':
    app.run(debug=True)
