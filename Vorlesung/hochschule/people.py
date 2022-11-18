class Student:
    def __init__(self,
                 name: str,
                 age: int,
                 course: str,
                 grade: int = None,
                 hobby: str = None):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade
        self.hobby = hobby


class Lecturer:
    def __init__(self, name: str, subjects: list[str]):
        self.name = name
        self.subjects = subjects

    @staticmethod
    def grade_student(student: Student, grade: float):
        student.grade = grade
