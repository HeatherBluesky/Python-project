from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_blueprint = Blueprint("books", __name__)

@book_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books = books)

@book_blueprint.route("/books/<id>")
def show(id):
    author = author_repository.select(id)
    return render_template("books/show.html", author=author)