# find the most common character in below string
from collections import Counter
from pprint import pprint

sentence = "This is a common interview question"

listify = list(sentence)


print(Counter(listify))

# answer is 'i' and '' both have 5
example = "This is a common interview question"

char_num = {}
for char in example:
    if char in char_num:
        char_num[char] += 1
    else:
        char_num[char] = 1

pprint(char_num, width=1)

fixed = sorted(
    char_num.items(), 
    key=lambda kv: kv[1], reverse=True)

print(fixed[0])