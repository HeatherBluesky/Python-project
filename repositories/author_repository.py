from db.run_sql import run_sql

from models.author import Author
from models.book import Book

def save(author):
    sql = "INSERT INTO author (first_name, last_name) VALUES ( %s, %s) RETURING *"
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author


def select(id):
    author = None
    sql = "SELECT * from authors WHERE id = %s"
    values = [id]
    results= run_sql (sql, values)
    if results:
        result = results[0]
        author = Author(result['first_name', 'last_name'])
    return author
                        

def update(author):
    sql = "UPDATE author SET ( first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [ author.first_name, author.last_name ,author.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM authors where id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE * FROM authors"
    run_sql(sql)

def get_books(author):
    books = []
    author_id = author.id
    sql = "SELECT * FROM books WHERE author_id = %s"
    values = [author_id]
    results = run_sql(sql, values)

    for row in results:
        book = Book(row['title'], row['author'], row['genre'], row['quanity'], row['buying_price'], row['selling_price'], row['language'], row['id'])
        books.append(book)
    return books
