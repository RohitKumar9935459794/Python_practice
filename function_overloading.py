class Squre:
    side=12
    def calculate_Area(self):
      return self.side*self.side

class Rightangle:
    len=12
    wid=24
    def calculate_Area(self):
        return self.len*self.wid

class  triangle:
    base=12
    height=11
    def calculate_Area(self):
        return 1/2*(self.height*self.base)


class circle:
    pi=3.14
    rad=11.0
    def calculate_Area(self):
        return self.pi*self.rad*self.rad

sq=Squre()
rg=Rightangle()
tri=triangle()
cr=circle()

print(sq.calculate_Area())
print(rg.calculate_Area())
print(rg.calculate_Area())
print(cr.calculate_Area())