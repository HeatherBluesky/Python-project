class Book:
    def __init__(self, title, author, genre, quantity, buying_price, selling_price, language, description, id = None):
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quantity
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.language = language
        self.description = description
        self.id = id