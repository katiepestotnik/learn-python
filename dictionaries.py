# key value pairs map keys to values

# key name -> value contact
#immutable types for keys value can be any type

point = {'x': 1, "y": 2}

point_1 = dict(x=1, y=2)

print(point_1["x"])

point_1["x"] = 10

print(point_1["x"])

point_1["z"] = 20

print(point_1)
# prints none if doesn't exist
# can add a second default argument is "a doesn't exist"
print(point_1.get("a", 0))
# delete pair
del point_1["x"]
print(point_1)

# looping
for key in point_1:
    print(key, point_1[key])

# returns tuple with items()
for x in point_1.items():
    print(x)
# returns str
for key, value in point_1.items():
    print(key, value)
    
# dictionary comprehensions

values = []
# for x in range(5):
#     values.append(x * 2)

# same as above  
# [expression for item in range(5)]
# list
comp_values = [x * 2 for x in range(5)]
print(comp_values)

# set
set_values = {x * 2 for x in range(5)}
print(type(set_values))

# dict
dict_values = {x: x * 2 for x in range(5)}
print(dict_values)

