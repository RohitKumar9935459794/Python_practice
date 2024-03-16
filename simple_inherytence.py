class Parent_class:
    def featre_1(self):
        print("this is feature one")

    def featre_2(self):
        print("this is featre two")

class Child_class(Parent_class):
    def featre_3(self):
        print("this is feature three")

child_obj=Child_class()
child_obj.featre_1()
child_obj.featre_2()
child_obj.featre_3()