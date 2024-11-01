class Person:

    def __init__(self, id, name, lastName, birthDate):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.birthDate = birthDate


    def describeUser(self):
        return print(f"Name: {self.name}\nLast Name: {self.lastName}\nBirth Date: {self.birthDate}")