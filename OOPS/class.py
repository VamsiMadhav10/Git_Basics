class Student:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age

    def __str__(self):
        return f"object of student class"
    
    def display(self):
        return f"Name of the student is {self.fname}"
    
    
s1=Student("Vamsi","Madhav",20)
print(s1.display())