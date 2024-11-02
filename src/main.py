from data.books import books
from data.users import users

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

        if (eleccion == 1):
            bookId = input("\n\n            ID del libro: ")
            self.getBookById(bookId)

        elif (eleccion == 2):
            title = input("\n\n            Título del libro: ")
            self.lendBookByTitle(title)

        elif (eleccion == 3):
            author = input("\n\n            Autor del libro: ")
            self.lendBookByAuthor(author)

        elif (eleccion == 4): self.generalMenu()
        else: print("\n\n            Opción no válida, por favor intenta de nuevo.")
        self.lendBookMenu()

    def returnBookMenu(self):
        userId = input("\n\n            Porfavor digita el id del usuario que va a regresar el libro: ")
        self.validateUser(userId)

    def lendBookById(self, id):
        pass

    def lendBookByTitle(self, title):
        bookFound = None

        for book in books["ebooks"] + books["physical_books"]:
            if book.title.lower() == title.lower():
                bookFound = book
                break

        if bookFound:
            print("\n\n            ¡Libro encontrado, que lo disfrutes! \n", bookFound)
            self.generalMenu()
        else:
            print("Libro no encontrado")

    def lendBookByAuthor(self, author):
        bookFound = None

        for book in books["ebooks"] + books["physical_books"]:
            if book.author.lower() == author.lower():
                bookFound = book
                break

        if bookFound:
            print("\n\n            ¡Libro encontrado, que lo disfrutes! \n", bookFound)
            self.generalMenu()
        else:
            print("Libro no encontrado")

    def getUserById(self, id):
        pass

    def getBookById(self, id):
        bookFound = None

        for book in books["ebooks"] + books["physical_books"]:
            if book.id == id:
                bookFound = book
                break

        if bookFound:
            print("\n\n            ¡Libro encontrado, que lo disfrutes! \n", bookFound)
            self.generalMenu()
        else:
            print("Libro no encontrado")

    def getBookByTitle(self, title):
        pass

    def getBookByAuthor(self, author):
        pass

# TO DO: FIX THIS METHOD
    def validateUser(self, id):
        user = None

        for user in users["students"]:
            if user.id == id:
                print(user.name)
                user = user
                pass

        for user in users["teachers"]:
            if user.id == id:
                print(user.name)
                user = user
                pass

        if user:
            print(user.booksLimit)
            if user.booksBorrowed == 5:
                print("Usuario ya tiene 5 libros prestados")
                self.generalMenu()
            

            elif user.booksBorrowed == 3:
                print("Usuario ya tiene 3 libros prestados")
                self.generalMenu()
            else: 
                print(f"El usuario tiene {user.booksBorrowed} prestadosssss")
                self.generalMenu()

        else:
            print("Usuario no encontrado")
            self.generalMenu()

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

        if (eleccion == 3):
            return
        elif (eleccion == 1):
            self.lendBookMenu()
        elif (eleccion == 2):
            self.returnBookMenu()
        else: print("\n\n            Opción no válida, por favor intenta de nuevo.")
        self.generalMenu()

project = Main()

project.generalMenu()
