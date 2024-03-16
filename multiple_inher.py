class Parent_class1:
    def featre(self):
        print("this is featre from parent class one")
    def featre_1(self):
        print("this is feature 1 from parent class 1 ")

class Parent_class2:
    def featre_2(self):
        print("this is deatre 0")

    def featre_3(self):
        print("this is deture 2")

class Child_class(Parent_class1,Parent_class2):
    def featre_4(self):
        print("this is feature 4 from child class")
        
child_obj=Child_class()
child_obj.featre()
child_obj.featre_1()
child_obj.featre_2()
child_obj.featre_3()
child_obj.featre_4()