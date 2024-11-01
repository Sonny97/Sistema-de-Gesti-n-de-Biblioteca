from models.people.Student import Student
from models.people.Teacher import Teacher

users = {
    "students": [
        Student("S1", "Alice Smith", "Smith", "1990-01-01", [], "Computer Science"),
        Student("S2", "Bob Johnson", "Johnson", "1991-02-02", [], "Mathematics"),
        Student("S3", "Charlie Brown", "Brown", "1992-03-03", [], "Literature"),
        Student("S4", "Diana Prince", "Prince", "1993-04-04", [], "History"),
        Student("S5", "Ethan Hunt", "Hunt", "1994-05-05", [], "Engineering")
    ],
    "teachers": [
        Teacher("T1", "Professor X", "X", "1970-01-01", []),
        Teacher("T2", "Dr. Who", "Who", "1971-02-02", []),
        Teacher("T3", "Mary Poppins", "Poppins", "1972-03-03", []),
        Teacher("T4", "Harry Potter", "Potter", "1973-04-04", []),
        Teacher("T5", "Tony Stark", "Stark", "1974-05-05", [])
    ]
}
