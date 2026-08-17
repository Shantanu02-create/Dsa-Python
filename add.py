#instance variable depends on object means it creates separate memory
#For each object
class Student:
    def __init__(self,rollno):
        self.rollno=rollno

    def display(self):
        print(self.rollno)
obj1=Student(100)
obj2=Student(102)
obj3=Student(103)
obj1.display()
obj2.display()
obj3.display()
obj1.rollno=200
obj1.display()
        