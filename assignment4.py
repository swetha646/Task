class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * 3.14
    def circumference(self):
        return 2 * 3.14 * self.radius
    def diameter(self):
        return 2 * self.radius

radius = int(input("enter the radius : "))
cir = Circle(radius)
print("Area of the cicle  :",cir.area())
print("circumference is : ",cir.circumference())
print("diameter is : ",cir.diameter())

    