#strings, numbers, booleans are immutable

learn ="Python"
# pass strings, lists
print(len(learn))
print(learn[0])
#returns first character from the end
print(learn[-1])
#returns second character from the end
print(learn[-2])
#slice (start index, end index) but not including end index value
print(learn[0:3])
#entire string
print(learn[0:])
print(id(learn))
print(id(learn[0]))

#\"
#\'
#\\
#\n prints on new line
#escape characters
escape = "python\n \"Escape\""
print(escape)

triple = """Python
Programming
"""
print(triple)

first = "Katie"
last = "Pestotnik"
#full = first + ' ' + last
#print(full)
#formatted strings
full =f"{first} {last}"
print(full)
# capitalize, upper, lower, title
ringo = "FUN class"
(ringo.upper())
print(ringo.title())
#useful for user input removes what space
print(ringo.strip())
#case sensitive if doesn't match get -1
#returns index of first character
print(ringo.find("FU"))
#replace (remove, put)
print(ringo.replace('FUN', '**'))
#check existence
print("FUN" in ringo)
#check not exist
print("**" not in ringo)
