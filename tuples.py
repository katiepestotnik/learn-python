# read only list cannot modify/add/remove
# use to not accidentally change data


point = (1, 2) + (3, 4)
print(point)

multi = (1, 2) * 3
print(multi)

#covert list or string to tuple
list_covert = tuple([1, 2])
print(list_covert)
# use index
print(list_covert[0])
# unpacking
x, y = list_covert
print(x)

# swapping variables with tuple

swap = 10
other_swap = 20
# defining a tuple since comma
swap, other_swap = other_swap, swap

print(swap, other_swap)