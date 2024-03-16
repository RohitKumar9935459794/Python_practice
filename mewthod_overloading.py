
# here we creating class squre
class Squre:
    side=25
    def calculate_Area(self):
        return self.side*self.side

class Triangle:
    height=12
    base=12
    def calculate_Area(self):
        return 1/2*(self.height*self.base)

sq=Squre()
tri=Triangle()

#we created two method with same name in different class so can we achive method overloading
print(sq.calculate_Area())
print(tri.calculate_Area())

#for(obj in(sq,tri)):
 #   obj.calcualte_Area()