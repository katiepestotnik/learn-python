# for large sequence of number less memory and a bit faster 10,000 + data items
from array import array
# array typecode for first argument

numbers = array("i", [1, 2, 3])

numbers.append(5)
print(numbers)