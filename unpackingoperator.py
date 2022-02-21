numbers = [1, 2, 3]
print(numbers)
# prints list
# if you want the individual numbers use unpacking operator
# same as spread operator in JS

print(*numbers)

# use for creating lists
# range object
range(5)
# convert to list
print(list(range(5)))

# instead unpacking operator possible with any iterable
print(*range(5))

print([*range(5), *"hello"])


first = [1, 2]
second = [3, 4]
values = [*first, 'and', *second]
print(values)


# combine dictionaries
# note that if same key will only get the last value
diction = {"x": 1}
diction_2 = {"x": 10, "y": 2}
combined = {**diction, **diction_2, "z": 1}
print(combined)