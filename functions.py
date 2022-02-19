# default by in params
# tuple cannot modify use () instead []
def increment(num: int, by: tuple = 1) -> int:
    return (num, num * by)


print((increment(num=2, by=3)))

# by=3 makes more readable

# * signifies tuple so we can iterate


def multiply(*list):
    total = 1
    for item in list:
        total *= item
        print(item)
    return (total)


print(multiply(3, 3, 3, 3))

# signifies dictionary(obj)

print('enter name')


def save_user(**user):
    print("user's name:", user["name"], "id:", user["id"])


save_user(name=input(''), id=1)
# global
message = 'hello'
print(message)
def greet():
    # turns local into global
    global message
    # local var
    message = 'what?'
    print(message)


greet()


def multi(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("start")
print(multi(1, 2, 3))
print("finish")
