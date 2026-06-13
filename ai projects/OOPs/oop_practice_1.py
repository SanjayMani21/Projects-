class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks= marks

   
    def grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >=50:
            return  'C'
        else:
            return 'F'

    def is_pass(self):
        if self.grade() != "F":
            return True
        else:
            return False
        
        

    def __str__(self):
        return f"{self.name} has scored {self.marks} marks. Grade is {self.grade()}. Status is {'Passed' if self.is_pass() else 'Failed'}"
    


students = []
pass_count = 0
fail_count = 0

data= ({'name': 'sanjay', 'marks':90},{'name': 'rahul', 'marks':45},{'name': 'priya', 'marks':80},{'name': 'arun', 'marks':60})

for student in data:
    name = student['name']
    marks = student['marks']
    
    stud = Student(name,marks)

    students.append(stud)

for i in students:
    print(i)
    if i.is_pass():
        pass_count +=1
        # print(pass_count)
    else :
        fail_count += 1 
        # print(fail_count)
print()
print(f'No of students Passed: {pass_count},\nNo of students Failed: {fail_count}')

    





