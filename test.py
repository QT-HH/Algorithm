class Student:
    def __init__(self,name):
        self.name = name

    def printName(self):
        print(self.name)

class GraduateStudent(Student):
    # def __init__(self,major):
    #     # self.name = name
    #     self.major = major

    def printMajor(self):
        print(self.major)

s1 = Student('홍길동')
s2 = GraduateStudent('컴퓨터')

s1.printName()
s2.printName()
s2.printMajor()
