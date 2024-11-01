from .Person import Person

class Student(Person):

    def __init__(self, id, name, lastName, birthDate, borrowedBooks, career, booksLimit, booksBorrowed):
        self.borrowedBooks = borrowedBooks
        self.career = career
        super().__init__(id, name, lastName, birthDate, booksLimit, booksBorrowed)