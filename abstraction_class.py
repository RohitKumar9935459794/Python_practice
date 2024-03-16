from abc import ABC

class Area(ABC):
    def circle_Area(self):
        pass
    def rightane_Area(self):
        pass
    def squre_Area(self):
        pass

class Circle(Area):
    rad=12
    pi=3.14
    def circle_Area(self):
        return self.rad*self.rad*self.pi

class Rightangle(Area):
    lenth=12
    wid=12
    def rightane_Area(self):
        return self.lenth*self.wid

class Squre(Area):
    side=6
    def squre_Area(self):
      return  self.side*self.side

cr=Circle()
ri=Rightangle()
sq=Squre()

print(cr.circle_Area())
print(ri.rightane_Area())
print(sq.squre_Area())

