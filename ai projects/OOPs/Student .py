# Exercise 1

# Student + Classroom

# Student
# ↓
# Classroom

# Features:

# Find passed students
# Find failed students
# Find toppers

student_data = [
    {"name": "Alice", "marks": 85 , "class": "10A"},
    {"name": "Bob", "marks": 35, "class": "10B"},
    {"name": "Charlie", "marks": 60, "class": "10A"},
    {"name": "David", "marks": 25, "class": "10B"},
    {"name": "Eve", "marks": 90, "class": "10A"}
    ]

class Student:
    def __init__(self, name, marks,class_name):
        self.name = name
        self.marks = marks
        self.class_name = class_name

    def is_passed(self):
        return self.marks >= 40
    
students = []
for student in student_data:
    s = Student(student["name"], student["marks"], student["class"])
    students.append(s)

    
class Classroom:
    def __init__(self, students):
        self.students = students
    
    def find_passed_students(self):
        passed_students = []
        for student in self.students:
            if student.is_passed():
                passed_students.append(student)
        return passed_students
    
    def find_failed_students(self):
        failed_students = []
        for student in self.students:
            if not student.is_passed():
                failed_students.append(student)
        return failed_students
    
    def toppers(self):
        topper = []
        max_marks = max(student.marks for student in self.students)
        for student in self.students:
            if student.marks == max_marks:
                topper.append(student)
        return topper

classroom = Classroom(students)
classroom_passed_students = classroom.find_passed_students()
print("Passed Students:")
for student in classroom_passed_students:
    print(f"Name: {student.name}, Marks: {student.marks}, Class: {student.class_name}")

classroom_failed_students = classroom.find_failed_students()
print("\nFailed Students:")
for student in classroom_failed_students:
    print(f"Name: {student.name}, Marks: {student.marks}, Class: {student.class_name}")

classroom_toppers = classroom.toppers()
print("\nTopper(s):")
for student in classroom_toppers:
    print(f"Name: {student.name}, Marks: {student.marks}, Class: {student.class_name}") 