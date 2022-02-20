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

