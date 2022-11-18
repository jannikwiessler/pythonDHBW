from people import Student, Lecturer
from building import University

if __name__ == "__main__":
    tobias = Student(name="Tobias", age=25, course="Data Science")
    lena = Student(name="Lena", age=22, course="Data Science")
    joe = Student(name="Joe", age=23, course="Application Management")

    jannik = Lecturer(name="Jannik", subjects=["Python1", "Python2", "C", "Computer Science"])
    marlen = Lecturer(name="Marlen", subjects=["Math1", "Math2", "Math3"])

    courses = {"Python1":
                   {"students": [tobias, lena, joe],
                    "lecturer": jannik},
               "Math1": {"students": [tobias, lena],
                         "lecturer": marlen}
               }
    dhbw = University(location="Loerrach", rooms=20, courses=courses)

    jannik.grade_student(student=tobias, grade=1.5)
    print(tobias.grade)
