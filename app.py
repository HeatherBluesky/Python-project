from flask import Flask, render_template

from controllers.book_shop_controller import author_blueprint
from controllers.book_controller import book_shop_blueprint


app = Flask(__name__)

app.register_blueprint(author_blueprint)
app.register_blueprint(book_shop_blueprint)

# @app.route('/')
# def hello_world():
#     return 'HELLO WORLD' 

if __name__ == '__main__':
    app.run(debug=True)