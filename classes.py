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

# inheritance
# parent base class
class Animal:
    def __init__(self):
        print('animal constructor')
        self.age = 1
    
    def eat(self):
        print("eat")

# child sub base class
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("mammal constructor")
        self.weight = 2
        
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")


mammal = Mammal()
print(type(mammal))
print(isinstance(mammal, object))
# problem below doesn't read mammal as class?
#print(issubclass(mammal, Animal))


print(mammal.age)
print(mammal.weight)

# multi level inheritance is a bad idea below complicated 1 level inheritance is better practice

class Animal:
    def eat(self):
        print('eat')

class Bird(Animal):
    def fly(self):
        print("fly")
        
class Chicken(Bird):
    pass


# multiple inheritance can cause issues

class Employee:
    def greet(self):
        print('hello')

class Person:
    def greet(self):
        print("person hello")
    
class Manager(Employee, Person):
    pass

manager = Manager()
# got employee because that is listed first in argument
manager.greet()

# better to use when the classes have nothing in common

# good example

class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

class FlyingFish(Flyer, Swimmer):
    pass

