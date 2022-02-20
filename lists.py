# can have different types of objects in list list numbers and strings
# string list
letters = ['a', 'b']
# matrix list two dimensional list
matrix = [[0, 1], [2, 3]]
# math operators on lists
zeros = [0] * 5
print(zeros)
combined = zeros + matrix
print(combined[6][0])
# 0 - 19
nums = list(range(20))
print(type(nums))
string = "Hello Computer"
print(list(string))
print(len(string))

letters = ['a', 'b', 'c', 'd']
# last item in list
letters[0] = "AB"
print(letters[-1])
print(letters)
# slice does not change the original
print(letters[0: 2])
# copy of original 
print(letters[:])
numbers = list(range(20))
# step, every other element
print(numbers[::2])
# return copy of original but in reverse
print(numbers[::-1])
print(numbers)

unpack_numbers = [1, 2, 3]

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]
# list unpacking same as above
first, second, third = unpack_numbers
print(first)

other_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# first two have variable and the rest packing in in other with the * syntax
# one, two, *other = other_numbers

# get first and last
one, *other, last = other_numbers
print(one, last)
print(other)

chars = ['a', 'b', 'c']
# looping and getting a tuple with the index and letter  with enumerate
for letter in enumerate(chars):
    # letter
    print(letter[1])
    # index of letter
    print(letter[0])


# simplify with unpacking tuple
for index, letter in enumerate(chars):
    print(index, letter)
    

alpha = ["a", "b", "c"]
# add to end
alpha.append('d')
print(alpha)
# add to specific position(index, what to add)
alpha.insert(1, "-")
print(alpha)
# remove at end or (index of item to remove)
alpha.pop()
print(alpha)
# only the first occurance is removed
alpha.remove('-')
print(alpha)
# remove by index or range
del alpha[0:2]
print(alpha)
# remove all
alpha.clear()
print(alpha)

alpha = ['a', 'b', 'c']
# find index if/in to prevent error if value doesn't exist
if 'd' in alpha:
    print(alpha.index('d'))
# count occurances
print(alpha.count('a'))


sort = [3, 17, 88, 3, 5]
# sort ascending order mutates original
# sort.sort()
# reverse by reverse parameter mutates original
sort.sort(reverse=True)
# return new list does not change original
print(sorted(sort, reverse=True))
print(sort)

items = [
    ("Product1", 10),
    ("Product2", 4),
    ("Product3", 20)
]
# function to sort only the numbers
# def sort_item(item):
#     return item[1]

# lambda function/anonymous don't need to make another function
items.sort(key=lambda item: item[1])
# items.sort(key=sort_item)
print(items)

# map
products = [
    ("Product1", 10),
    ("Product2", 4),
    ("Product3", 20)
]
prices = []
for product in products:
    prices.append(product[1])
print(prices)

# returns map object
x = list(map(lambda product: product[1], products))
# for product in x:
#     print(product)
print(x)

# filter
groceries = [
    ("OJ", 5),
    ("Bread", 4),
    ("Shrimp", 10)
]
# returns filter object
x = list(filter(lambda item: item[1] >= 5, groceries))

# returns a list with any tuple that matches
print(x)

# can use instead of map and filter functions
# list comprehensions / same as above shorter and cleaner
print([item[1] for item in groceries])
# get booleans for each 
print([item[1] >= 5 for item in groceries])
# get just the items that match expression
print([item for item in groceries if item[1] >= 10])


# zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]
# trying to get to combine lists
[(1, 10), (2, 20), (3, 30)]

print(list(zip("abc", list1, list2)))

# stacks LIFO (last in first out)
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])
if not browsing_session:
    print('disable')
    

# queues FIFO first in first out
from collections import deque
q = deque([])
q.append(1)
q.append(2)
q.append(3)
q.popleft()
print(q)
if not q:
    print('empty')