import datetime
import random


class Student:
    def __init__(self, name: str, birthdate: datetime):
        self.name = name
        self.age = datetime.datetime.now().year - birthdate.year
        self.__birthdate = birthdate
        self.grade = None


class Lecturer:
    def __init__(self, name, birthdate, students):
        self.name = name
        self.age = datetime.datetime.now().year - birthdate.year
        self.__students = students
        self.__birthdate = birthdate

    def grade_students(self):
        for student in self.__students:
            student.grade = random.randint(1, 6)

    def show_grades(self):
        for student in self.__students:
            print(f"Student: {student.name}, grade: {student.grade}")


if __name__ == "__main__":
    tom = Student(name="Tom", birthdate=datetime.date(1999, 10, 28))
    lea = Student(name="Lea", birthdate=datetime.date(1998, 5, 28))
    joe = Student(name="Joe", birthdate=datetime.date(2001, 5, 21))
    student_list = [tom, lea, joe]
    ron = Lecturer(name="Ron", birthdate=datetime.date(1994, 2, 17), students=student_list)
    ron.grade_students()
    ron.show_grades()

