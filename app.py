from flask import Flask, render_template

from controllers.book_shop_controller import book_Shop_blueprint


app = Flask(__name__)

app.register_blueprint(book_Shop_blueprint)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)