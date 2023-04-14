import pdb
from models.book import Book 
from models.author import Author 
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository


author_1 = Author("Bilbo", "Baggins")
author_repository.save(author_1)

author_2 = Author("Frodo" ,"Baggins")
author_repository.save(author_2)

book_1 = Book("There and Back Again: A Hobbits Tale", author_1, "Biolgraphy", 10, 4.50, 14.99)
book_repository.save(book_1)

book_2 = Book("Middle Earth, A Travel Guide", author_2, "Travel", 7, 3.50, 9.99)
