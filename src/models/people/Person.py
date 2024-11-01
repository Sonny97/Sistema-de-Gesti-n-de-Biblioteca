class Person:

    def __init__(self, id, name, lastName, birthDate, booksLimit, booksBorrowed):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.birthDate = birthDate
        self.booksLimit = booksLimit
        self.booksBorrowed = booksBorrowed


    def describeUser(self):
        return print(f"Name: {self.name}\nLast Name: {self.lastName}\nBirth Date: {self.birthDate}\n Books Limit: {self.booksLimit} \n Books Borrowed: {self.booksBorrowed}")