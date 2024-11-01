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
        return print(f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}\nDescription: {self.description}\nQuantity: {self.quantity}\nPublication Year: {self.publicationYear}")

    def validateQuantity(self):
        if self.quantity > 0:
            return True
        else:
            return False