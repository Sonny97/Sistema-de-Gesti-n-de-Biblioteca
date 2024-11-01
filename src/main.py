from models.books.EBook import EBook
from models.books.PhysicalBook import PhysicalBook

class Main:

    def lendBookMenu(self):
        print("""
            =========================================
            |¿Cómo deseas buscar el libro a prestar?|
            =========================================

                1. Buscar por ID
                2. Buscar por Título
                3. Buscar por Autor
                4. Volver al menú anterior
            """)

        eleccion = int(input("            Por favor, ingresa el número de tu elección: "))

        if(eleccion == 1): self.getBookById()
        elif (eleccion == 2): self.lendBookByTitle()
        elif (eleccion == 3): self.lendBookByAuthor()
        else: self.generalMenu()

    def returnBookMenu(self):
        userId = input("\n\n            Porfavor digita el id del usuario que va a regresar el libro: ")
        validation = self.validateUser(userId)
        if(~validation):
            print("Usuario no existe, volviendo al menu anterior...")
        else: print("devuelto")


    def lendBookById(self, id):
        pass

    def lendBookByTitle(self, title):
        pass

    def lendBookByAuthor(self, author):
        pass

    def getUserById(self, id):
        pass

    def getBookById(self, id):
        pass

    def getBookByTitle(self, title):
        pass

    def getBookByAuthor(self, author):
        pass

    def validateUser(self, id):
        pass

    def goBack(self):
        pass

    def generalMenu(self):
        print("""
            ======================================
            | Bienvenido al Sistema de Préstamos |
            ======================================

            ¿Qué te gustaría hacer?

                1. Prestar un libro
                2. Devolver un libro
                3. Salir del programa
            """)

        eleccion = int(input("            Por favor, ingresa el número de tu elección: "))

        if(eleccion == 1):
            self.lendBookMenu()
        elif (eleccion == 2): self.returnBookMenu()
        else: return

    sobreviviendoAEscobar = EBook("0", "Sobreviviendo a Escobar", "JJ", "100", "un libro mas", "3", "2020")
    LaBiblia = EBook("1", "La Santa Biblia", "Diosito", "1000", "el libro de la vida", "100", "0")
    LaBiblia = PhysicalBook("1", "La Santa Biblia", "Diosito", "100", "el libro de la vida", "100", "0", False)


project = Main()

project.generalMenu()