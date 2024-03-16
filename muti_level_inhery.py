class Parent_1:
    def featre_1(self):
        print("this is parent one  child")
    def featre_2(self):
        print("this is parent featre  two  from parent one")

class Parent_2(Parent_1):
    def method_1(self):
     print(" this is parent from two")
obj=Parent_2()
obj.featre_1()
obj.featre_2()

class Child_class(Parent_2):
    def child_feature(self):
        print("this is child featre")
child_obj=Child_class()
child_obj.featre_1()
child_obj.featre_2()
child_obj.method_1()
child_obj.child_feature()