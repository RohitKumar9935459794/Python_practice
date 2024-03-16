#instance variable: when the varible get intionaize when objevt ids created

class Student:
    def __init__(self,a,b):
        self.a=a
        self.b=b

#creating out side method
    def avg(self):
     return (self.a+self.b)/2

s1=Student(10,20)
print(s1.avg())
