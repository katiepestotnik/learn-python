# __init__
# __str__

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# point = Point(1, 2)
# print(point)

#compare objects

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # equality  
    def __eq__(self, comp_obj):
        return self.x == comp_obj.x and self.y == comp_obj.y
    # greater than
    def __gt__(self, comp_obj):
        return self.x > comp_obj.x and self.y > comp_obj.y
    # add
    def __add__(self, comp_obj):
        return self.x + comp_obj.x and self.y + comp_obj.y

point = Point(2, 3)
other = Point(1, 2)
# false due to two different locations in memory must use magic methods to get return of true
print(point == other)
print(point > other)
print(point.x + other.x)

# fix case sensitivity
# custom containers
# cloud = TagCloud()
# len(cloud)
# cloud["python"] = 10
# for tag in cloud:
#     print(tag)

class TagCloud:
    def __init__(self):
        self.tags = {}
        
    def add(self, tag):
        self.tags[tag.lower()]= self.tags.get(tag.lower(), 0) + 1
    
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count
    
    def __len__(self):
        return len(self.tags)
    
    def __iter__(self):
        return iter(self.tags)

cloud = TagCloud()
cloud["python"] = 10
cloud.add('Python')
cloud.add('python')
cloud.add('python')
print(cloud.tags)

# harder to access values if you use __beforevariable
