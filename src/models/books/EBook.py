from .Book import Book

class EBook(Book):

    def __init__(self, id, title, author, pages, description, quantity, publicationYear):
        super().__init__(id, title, author, pages, description, quantity, publicationYear)


    def download(id):
        pass