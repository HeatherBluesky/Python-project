import pdb
from models.book import Book 
from models.author import Author 
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository


author_1 = Author("Bilbo", "Baggins")
author_repository.save(author_1)

author_2 = Author("Frodo" ,"Baggins")
author_repository.save(author_2)

author_3 = Author("Khal", "Drogo")
author_repository.save(author_3)

author_4 = Author("Loki", "God of Mischief")
author_repository.save(author_4)


book_1 = Book("There and Back Again: A Hobbits Tale", author_1, "Autobiography", 10, 4.50, 14.99, "Hobbitish")
book_repository.save(book_1)

book_2 = Book("Middle Earth, A Travel Guide", author_2, "Travel", 7, 3.50, 9.99, "Hobbitish")
book_repository.save(book_2)

book_3 = Book("Horse Handling for Dummiess", author_3, "Education", 3, 3.49, 8.99, "Dothraki")
book_repository.save(book_3)

book_4 = Book("I am Burdened with Glorious Purpose", author_4, "Autobiography", 6, 4.99, 14.99, "Asguardian")
book_repository.save(book_4)

pdb.set_trace()