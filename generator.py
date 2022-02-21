# infinite data or very large data
# can't get the total number of items no len()
# don't store in memory generate new value in each iteration
# size remains the size no matter the range of numbers gen: 120
# change [] to ()
from sys import getsizeof

values = (x * 2 for x in range(100000))
print("generater: ", getsizeof(values))
print(values)
# 104 bytes
values = [x * 2 for x in range(100000)]
print("list: ", getsizeof(values))
# 800984 bytes