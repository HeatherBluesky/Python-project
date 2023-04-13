class Book:
    def __init__(self, title, author, genre, quanity, buying_price, selling_price,  id = None):
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quanity
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.id = id