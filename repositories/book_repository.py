from db.run_sql import run_sql
from repositories import author_repository
from models.book import Book

def save(book):
    sql = "INSERT INTO books (title, author_id, genre, quantity, buying_price, selling_price, language) VALUES ( %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [book.title, book.author.id, book.genre, book.quantity, book.buying_price, book.selling_price, book.language]
    results = run_sql(sql, values)
    book.id = results[0]['id']
    return book

def select_all():
    books = []
    sql = " SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book (row['title'], author, row['genre'], row['quantity'], row ['buying_price'], row['selling_price'], row['language'])
        books.append(book)
    return books

def update(book):
    sql = "UPDATE books SET ( title, author_id, genre, quantity, buying_price, selling_price, language) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [ book.title, book.author_id, book.genre, book.quantity, book.buying_price, book.selling_price, book.language, book.id]
    run_sql(sql, values)

def get_langauges(books):
    books = []
    book_language = book_language
    sql = "SELECT * FROM  books WHERE language = %s"
    values = [book_language]
    results = run_sql(sql, values)
    for row in results:
        book = Book(row['title'], row['author'], row['genre'], row['quantity'], row['buying_price'], row['selling_price'], row['language'], row['id'])
        books.append(book)
    return books


def delete(id):
    sql = "DELETE FROM books where id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE * from books"
    run_sql(sql)