from .Book import Book
import json

class PhysicalBook(Book):

    def __init__(self, id, title, author, pages, description, quantity, publicationYear, isBorrowed):
        self.isBorrowed = isBorrowed
        super().__init__(id, title, author, pages, description, quantity, publicationYear)

    def __str__(self):
        return json.dumps({
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "pages": self.pages,
            "description": self.description,
            "quantity": self.quantity,
            "publicationYear": self.publicationYear,
            "isBorrowed": self.isBorrowed
        }, indent=4)