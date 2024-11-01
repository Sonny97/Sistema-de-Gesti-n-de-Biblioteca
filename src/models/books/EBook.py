from .Book import Book
import json

class EBook(Book):

    def __init__(self, id, title, author, pages, description, quantity, publicationYear):
        super().__init__(id, title, author, pages, description, quantity, publicationYear)


    def download(self, id):
        pass

    def __str__(self):
        return json.dumps({
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "pages": self.pages,
            "description": self.description,
            "quantity": self.quantity,
            "publicationYear": self.publicationYear
        }, indent=4)
