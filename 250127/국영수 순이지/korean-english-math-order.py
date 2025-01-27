n = int(input())
name = []
korean = []
english = []
math = []

class Student:
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.math = int(math)

students = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))
    students.append(Student(student_info[0],student_info[1],student_info[2],student_info[3]))

students.sort(key = lambda x:(-x.kor,-x.eng,-x.math))

# Write your code here!

for i,items in enumerate(students):
    print(f"{items.name} {items.kor} {items.eng} {items.math}")

    
