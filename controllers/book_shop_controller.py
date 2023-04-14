from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_Shop_blueprint = Blueprint("books", __name__)

@book_Shop_blueprint.route("/shop_book")
def books():
    books = book_repository.select_all()
    return render_template("books_shop/index.html", books = books)