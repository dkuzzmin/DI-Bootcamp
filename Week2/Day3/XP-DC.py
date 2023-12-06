class Circle:
    def __init__(self, radius, diameter) -> None:
        self.radius = radius
        self.diameter = diameter
    @classmethod
    def from_radius(cls, radius):
        return cls(radius = radius, diameter = 2 * radius)
    @classmethod
    def from_diameter(cls, diameter):
        return cls(radius = diameter / 2, diameter = diameter)
            
    def circle_area(self):
        return 3.14 * self.radius**2
 
    def __str__(self):
         return f"Radius={self.radius}, diameter={self.diameter}, area={self.circle_area()}"

    def __add__(self, x):
        return self.diameter + x.diameter

    def __gt__(self, x):
        return self.radius > x.radius

    def __eq__(self, x):
        return self.radius == x.radius


cir1 = Circle.from_radius(70)
cir2 = Circle.from_diameter(50)
print(cir1.diameter)
print(cir2.radius)
print(cir1.circle_area())
print(cir1)
new_circle = cir1 + cir2
print(new_circle)


print(cir1 > cir2)
print(cir1 == cir2)

circles = [cir1, cir2]
circles.sort()
print(circles[0])
print(circles[1])