# blueprint for creating new objects
# object is an instance of a class

class Point:
    # class level attribute
    default_color = "red"
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #class method decorator(class)
    # Point(0, 0) # factory
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")




point = Point.zero()
print(point)
print(point.default_color)
print(Point.default_color)
# add a new attribute when needed
point.z = 10
point.draw()

another = Point(3, 4)
another.draw()

# print(type(point))
# prove instance of Point
# print(isinstance(point, Point))


