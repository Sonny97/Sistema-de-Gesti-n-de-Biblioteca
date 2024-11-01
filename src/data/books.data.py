from models.books.EBook import EBook
from models.books.PhysicalBook import PhysicalBook

ebooks = [
    EBook("E1", "Digital Fortress", "Dan Brown", "356", "A techno-thriller novel about cryptography.", "7", "1998"),
    EBook("E2", "The Lean Startup", "Eric Ries", "320", "Principles for startups to create efficient businesses.", "12", "2011"),
    EBook("E3", "Python Crash Course", "Eric Matthes", "544", "A hands-on, project-based guide to learning Python.", "8", "2015"),
    EBook("E4", "Clean Code", "Robert C. Martin", "464", "A handbook of agile software craftsmanship.", "5", "2008"),
    EBook("E5", "1984", "George Orwell", "328", "A dystopian novel set in a totalitarian society.", "15", "1949"),
    EBook("E6", "The Art of War", "Sun Tzu", "273", "An ancient Chinese military treatise.", "6", "5th century BC"),
    EBook("E7", "The Great Gatsby", "F. Scott Fitzgerald", "180", "A novel set in the Roaring Twenties.", "10", "1925"),
    EBook("E8", "Atomic Habits", "James Clear", "320", "A guide to building good habits and breaking bad ones.", "9", "2018"),
    EBook("E9", "The Catcher in the Rye", "J.D. Salinger", "277", "A novel about teenage rebellion and alienation.", "7", "1951"),
    EBook("E10", "To Kill a Mockingbird", "Harper Lee", "281", "A novel about racial injustice in the American South.", "12", "1960"),
    EBook("E11", "Pride and Prejudice", "Jane Austen", "432", "A classic romantic novel.", "8", "1813"),
    EBook("E12", "The Road", "Cormac McCarthy", "287", "A post-apocalyptic survival story.", "5", "2006"),
    EBook("E13", "Sapiens", "Yuval Noah Harari", "443", "A history of humankind.", "10", "2014"),
    EBook("E14", "Thinking, Fast and Slow", "Daniel Kahneman", "499", "A book on human psychology and decision-making.", "6", "2011"),
    EBook("E15", "The Subtle Art of Not Giving a F*ck", "Mark Manson", "224", "A guide to a counterintuitive approach to living a good life.", "9", "2016")
]

physical_books = [
    PhysicalBook("B1", "A Brief History of Time", "Stephen Hawking", "256", "A classic in popular science.", "3", "1988", False),
    PhysicalBook("B2", "The Hobbit", "J.R.R. Tolkien", "310", "A fantasy novel and precursor to the Lord of the Rings.", "7", "1937", False),
    PhysicalBook("B3", "The Da Vinci Code", "Dan Brown", "689", "A mystery thriller that explores historical secrets.", "5", "2003", True),
    PhysicalBook("B4", "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "309", "The first book in the Harry Potter series.", "12", "1997", False),
    PhysicalBook("B5", "Moby Dick", "Herman Melville", "635", "A classic tale of a sea captain's obsession.", "4", "1851", True),
    PhysicalBook("B6", "War and Peace", "Leo Tolstoy", "1225", "A historical epic novel.", "3", "1869", False),
    PhysicalBook("B7", "The Catcher in the Rye", "J.D. Salinger", "277", "A novel about teenage rebellion and alienation.", "7", "1951", True),
    PhysicalBook("B8", "Crime and Punishment", "Fyodor Dostoevsky", "671", "A psychological drama and moral dilemma.", "6", "1866", False),
    PhysicalBook("B9", "Frankenstein", "Mary Shelley", "280", "A Gothic novel about the dangers of scientific ambition.", "8", "1818", False),
    PhysicalBook("B10", "Don Quixote", "Miguel de Cervantes", "863", "The story of a nobleman's adventures.", "4", "1605", True),
    PhysicalBook("B11", "Great Expectations", "Charles Dickens", "505", "A coming-of-age story.", "10", "1861", False),
    PhysicalBook("B12", "Jane Eyre", "Charlotte Bronte", "500", "A novel about a woman's journey and independence.", "5", "1847", True),
    PhysicalBook("B13", "The Odyssey", "Homer", "560", "An epic poem from ancient Greece.", "9", "8th century BC", False),
    PhysicalBook("B14", "The Divine Comedy", "Dante Alighieri", "798", "A narrative poem about the afterlife.", "6", "1320", True),
    PhysicalBook("B15", "The Iliad", "Homer", "704", "A classic epic of war.", "7", "8th century BC", False)
]
