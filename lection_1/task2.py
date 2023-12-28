from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "home page"


# @app.route('/1/')
# @app.route('/2/')
# @app.route('/3/')
# def page_1():
#     return f"page 1"


# @app.route('/<page>/')
# def any_page(page):
#     return f"page {page}"


@app.route('/poems/')
def poems():
    poem = ['Вот не думал, не гадал,',
            'Программистом взял и стал.',
            'Хитрый знает он язык,',
            'Он к другому не привык.',
            ]
    txt = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return txt


if __name__ == '__main__':
    app.run(debug=False)
