class Parent_one:
    def __init__(self):
        self.age=12

    def method_1(self):
        print("this is method from parent one")
obj=Parent_one()
print(obj.age)

class Parent_two:
    def method_2(self):
        print("this is method from parent two")

class Child_class(Parent_one,Parent_two):
    def methode_3(self):
        print("this is method from child class ")
child_obj=Child_class()
child_obj.method_1()
child_obj.method_2()
child_obj.methode_3()
