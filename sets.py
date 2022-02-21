# collection with no duplicates
# sets wrap in {}

numbers = [1, 1, 2, 3, 4, 4]
uniques = set(numbers)
second = {1, 4}
second.add(10)
second.remove(1)
print(second)
print(len(second))
print(uniques)

# best for math operators

first = set(numbers)
# returns all uniques in both sets
print(first | second)
# returns any that are in both sets
print(first & second)

# what we dont have in the second set
print(first - second)
# either in first or second but not both
print(first ^ second)

# no indexing no order to numbers

if 1 in first:
    print('yes')