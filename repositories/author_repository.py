from db.run_sql import run_sql

from repositories import book_repository
from models.author import Author

def save(author):
    sql = "INSERT INTO author (first_name, last_name) VALUES ( %s, %s) RETURING id"
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    author.id = results[0]['id']
    return author