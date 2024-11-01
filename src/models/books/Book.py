class Book:
    def __init__(self, id, title, author, pages, description, quantity, publicationYear):
        self.id = id
        self.title = title
        self.author = author
        self.pages = pages
        self.description = description
        self.quantity = quantity
        self.publicationYear = publicationYear


    def describeBook(self):
        pass

    def validateQuantity(self):
        pass