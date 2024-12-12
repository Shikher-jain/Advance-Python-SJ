class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def area(self):
        return self.x*self.y
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)#override

    def area(self):
        # return 3.14 * self.radius*self.radius
        return 3.14 * super().area()#override
    
# rec=Shape(6,3)
cir=Circle(7)
# print(rec.area())
print(cir.area())