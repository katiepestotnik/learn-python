try:
    with open("./dictionaries.py") as file:
        print("file opened")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as error:
    print('must number great than 0')
    print(error)
    print(type(error))
else:
    print('no exceptions were thrown')
# with statement you do not need finally
# finally:
#     file.close()
print('program keeps running')

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError('age must be > 0')
    return 10 / age

try:
    calculate_xfactor(1)
except ValueError as error:
    print(error)
else:
    print('did not break')
    
