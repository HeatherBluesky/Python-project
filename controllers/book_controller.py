from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repositorty


book_shop_blueprint = Blueprint("books", __name__)

@book_shop_blueprint.route("/books/<id>")
def show(id):
    book = book_repository.select(id)
    language = book_repository.language(book)
    return render_template("books/show.html", book=book, languages=language)

@book_shop_blueprint.route("/books",  methods=['POST'])
def create_book():
    title    = request.form['title']
    genre = request.form['genre']
    author  = author_repositorty.select(request.form['author_id'])
    book = Book(title, author, genre, quantity, buying_price, selling_price, language)
    book_repository.save(book)
    return redirect('/books')

@book_shop_blueprint.route("/books/<id>", methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/show.html', book = book)

@book_shop_blueprint.route("/books/new", methods=['GET'])
def new_book():
    authors = author_repositorty.select_all()
    return render_template("books/new.html", all_authors = authors)

@book_shop_blueprint.route("/books/<id>/edit", methods=['GET'])
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repositorty.select_all()
    return render_template('books/edit.html', book = book, all_authors = authors)

@book_shop_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    title    = request.form['title']
    genre = request.form['genre']
    publisher   = request.form['publisher']
    author  = author_repositorty.select(request.form['author_id'])
    book = Book(title, genre, publisher, author, id)
    print(book.author.full_name())
    book_repository.update(book)
    return redirect('/books')


@book_shop_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')