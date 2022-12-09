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
        self.university = None

    def is_allowed_to_grade(self, student: Student):
        for course in self.university.courses.values():
            if course["lecturer"] == self and student in course["students"]:
                return True
        return False

    def grade_student(self, student: Student, grade: float):
        if self.is_allowed_to_grade(student=student):
            student.grade = grade
        else:
            print(f"Im am not allowed to grade {student.name}")


