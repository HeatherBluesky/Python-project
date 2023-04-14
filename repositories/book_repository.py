from db.run_sql import run_sql
from repositories import author_repository
from models.book import Book

def save(book):
    sql = "INSERT INTO books (title, author, genre, quanity, buying_price, selling_price, language) VALUES ( %s, %s, %s, %s, %s, %s, %s) RETURING id"
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