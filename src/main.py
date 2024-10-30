from models.books.EBook import EBook
from models.books.PhysicalBook import PhysicalBook

class main:
    
    def lendBookMenu():
        print(""" como deseas buscar el libro a prestar?
              1. para buscar por Id.
              2. para buscar por titulo.
              3. para buscar por author.
              *. para volver al menu anterior.
              """)
        
        eleccion = int(input())

        if(eleccion == 1): self.getBookById()
        elif (eleccion == 2): self.lendBookByTitle()
        elif (eleccion == 3): self.lendBookByAuthor()
        else: self.generalMenu()
    
    def returnBookMenu():
        print(""" Porfavor digita el id del usuario que va a regresar el libro""")
        userId = input()
        validation = self.validateUser(userId)
        if(~validation): 
            print("Usuario no existe, volviendo al menu anterior...")
        else: print("devuelto")
        

    def lendBookById(id):
        pass

    def lendBookByTitle(title):
        pass

    def lendBookByAuthor(author):
        pass

    def getUserById(id):
        pass

    def getBookById(id):
        pass

    def getBookByTitle(title):
        pass

    def getBookByAuthor(author):
        pass

    def validateUser(self, id):
        pass
 
    def goBack():
        pass

    def generalMenu(self):
        print(""" Bienvenido al sistema de prestamos, que deseas hacer?
              1. para prestar un libro.
              2. para retornar un libro.
              * para salir del programa.
              """)
        eleccion = int(input())

        if(eleccion == 1): 
            self.lendBookMenu()
        elif (eleccion == 2): returnBookMenu()
        else: return
    
    sobreviviendoAEscobar = EBook("0", "Sobreviviendo a Escobar", "JJ", "100", "un libro mas", "3", "2020")
    LaBiblia = EBook("1", "La Santa Biblia", "Diosito", "1000", "el libro de la vida", "100", "0")
    LaBiblia = PhysicalBook("1", "La Santa Biblia", "Diosito", "100", "el libro de la vida", "100", "0", False)
    generalMenu()