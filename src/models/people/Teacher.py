from .Person import Person

class Teacher(Person):

    def __init__(self, id, name, lastName, birthDate, borrowedBooks, booksLimit, booksBorrowed):
        self.borrowedBooks = borrowedBooks
        super().__init__(id, name, lastName, birthDate, booksLimit, booksBorrowed)