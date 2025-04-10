class Student:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    
    def display(self):
        return f"details of student-> Name:{self.fname} {self.lname} , Age: {self.age}"

class enrolled(Student):
