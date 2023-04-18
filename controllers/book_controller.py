from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repositorty
import pdb


book_shop_blueprint = Blueprint("books", __name__)

@book_shop_blueprint.route("/")
def books():
    books = book_repository.select_all()
    return render_template("/index.html", books = books)


@book_shop_blueprint.route("/books")
def all_books():
    print("method hit")
    books = book_repository.select_all()

    return render_template("books/index.html", books = books)

@book_shop_blueprint.route("/books/<id>")
def show(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book =book)

@book_shop_blueprint.route("/books/new", methods=['GET'])
def new_book():
    books = book_repository.select_all()
    authors = author_repositorty.select_all()
    return render_template("books/new.html", books = books, authors = authors)

@book_shop_blueprint.route("/books/new",  methods=['POST'])
def create_book():
    title = request.form['title']
    author  = author_repositorty.select(request.form['author_id'])
    genre = request.form['genre']
    quantity = request.form['quantity']
    buying_price = request.form['buying_price']
    selling_price = request.form['selling_price']
    language = request.form['language']
    book = Book(title, author, genre, quantity, buying_price, selling_price, language)
    book_repository.save(book)
    # return render_template("books/new.html")   
    return redirect('/books') 

@book_shop_blueprint.route("/books/<id>", methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/show.html', book = book)

@book_shop_blueprint.route("/books/<id>/edit", methods=['GET'])
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repositorty.select_all()
    return render_template('books/edit.html', book = book, all_authors = authors)

@book_shop_blueprint.route("/books/<int:id>", methods=['POST'])
def update_book(id):
    title = request.form['title']
    author = author_repositorty.select(request.form['author_id'])
    genre = request.form['genre']
    quantity = request.form['quantity']
    buying_price = request.form ['buying_price']
    selling_price = request.form['selling_price']
    language = request.form['selling_price']
    book = Book(title, author, genre, quantity, buying_price, selling_price, language, id)
    book_repository.update(book)
    return redirect('/books')


@book_shop_blueprint.route("/books/<int:id>/delete")
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')