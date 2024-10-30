from .Book import Book

class PhysicalBook(Book):

    def __init__(self, id, title, author, pages, description, quantity, publicationYear, isBorrowed):
        self.isBorrowed = isBorrowed
        super().__init__(id, title, author, pages, description, quantity, publicationYear)