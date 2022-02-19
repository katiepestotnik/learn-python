age = 17
if age >= 18:
    print("Adult")
    print("Enter")
elif age >= 13:
    print("teen")
else:
    print('child')

print('all done')

num = 20
if num > 21:
    # can't have empty condition
    pass
else:
    print('nope')

# logical operators
# and
# or
# not
# use .strip() to avoid incorrect values with whitespace
name = ' '
if not name.strip():
    print('Name is empty')

age = 17
if age >= 18 and age < 65:
    print("Ok")

# same as above
if 18 <= age < 64:
    print("shorter version")

# ternary operator
age_check = "Enter" if age >= 21 else "not old enough"
print(age_check)

# two types of loops
# for
# while

for x in "python":
    print(x)
for x in ['a', 'b', 'c']:
    print(x)

# last argument prints each num 0 + 2 and on
for x in range(0, 10, 2):
    print(x)
# not a list a range object small amount of memory
print(type(range(500000000000)))

names = ["Sally", "Larry", "laley"]
for name in names:
    if name.startswith("H"):
        print("Found")
        # leave loop after first found
        break
else:
    print('not found')

# while
guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
    print('wrong, try again')
else:
    print(f'winner! you guessed {guess}')