#the methid implement as python

class Student:
    name='Student'
    def __init__(self,a,b):
        self.a=a
        self.b=b

    @staticmethod
    def info():
       return "this is another"
       print(Student.info())

