from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author_blueprint = Blueprint("authors", __name__)

@author_blueprint.route("/authors")
def authors():
    authors =author_repository.select_all()
    return render_template("authors/index.html", authors = authors)

