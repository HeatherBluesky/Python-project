from db.run_sql import run_sql
from repositories import author_repository
from models.book import Book

def save(book):
    sql = "INSERT INTO books (title, author, genre, quanity, buying_price, selling_price) VALUES ( %s, %s, %s, %s, %s, %s) RETURING id"
    values = [book.title, book.author, book.genre, book.quantity, book.buying_price, book.selling_price]
    results = run_sql(sql, values)
    book.id = results[0]['id']
    return book