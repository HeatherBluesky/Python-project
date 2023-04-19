from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author_blueprint = Blueprint("authors", __name__)

@author_blueprint.route("/authors")
def authors():
    authors =author_repository.select_all()
    return render_template("authors/index.html", authors = authors)

@author_blueprint.route("/authors/<id>")
def show(id):
    author = author_repository.select(id)
    return render_template("authors/show.html", author =author)

@author_blueprint.route("/authors/<id>/edit", methods=['GET'])
def edit_author(id):
    author = author_repository.select(id)
    return render_template('authors/edit.html', author = author)

@author_blueprint.route("/authors/<int:id>", methods=['POST'])
def update_author(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    author = Author(first_name, last_name,id)
    author_repository.update(author)
    return redirect('/authors')

@author_blueprint.route("/authors/new", methods=['GET'])
def new_author():
    authors = author_repository.select_all()
    books = book_repository.select_all()
    return render_template("authors/new.html", books = books, authors = authors)

@author_blueprint.route("/authors/new",  methods=['POST'])
def create_author():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    author = Author(first_name, last_name)
    author_repository.save(author)
    return redirect('/authors') 

@author_blueprint.route("/authors/<int:id>", methods=['GET'])
def show_author(id):
    author = author_repository.select(id)
    return render_template('/authors/show.html', author = author)


@author_blueprint.route("/authors/<int:id>/delete")
def delete_author(id):
    author_repository.delete(id)
    return redirect('/authors')
