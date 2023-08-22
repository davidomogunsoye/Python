# TOPIC: String Methods
import math
import time

name = 'david'

print(name)
print(len(name))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count('d'))   # count recognizes letters differently if they are not of the same case
print(name.replace('a', 'e'))
print(name*3)

# TOPIC: type casting = converting the data type of value to another data type

x = 1  # int
y = 2.0  # float
z = '3'  # str

print(x)
print(y)
print(z)

print(int(y))  # typecasting within print will not make change permanent

y = int(y)  # doing this will
print(type(y))

print(x)
print(y)
print(z*3)

z = float(z)
y = float(y)
x = float(x)

print(x)
print(y)
print(z*3)

# TOPIC: Accepting User Input

name = input('What is your name?: ') # user prompted to input the variable called name
age = int(input('What is your age?: ')) #
typecast a number input to float or int to allow calculations, else it is entered as string
height = float(input('How tall are you?: '))

print('Hello '+name)
print('You are '+str(age)+' years old' ) #convert back to string to display with other string
print('You are '+str(height)+'cm tall')

# useful math functions (import math at beginning of file)

pi = 3.14

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 2))
print(math.sqrt(pi))
print(max(x, y, z))
print(min(x, y, z))

# TOPIC: string_slicing = creating a substring by extracting elements from another string
# can use indexing using [] or slice() fxn
# index requires 3 arguments [start: stop: step]

full_name = 'David Adewale'

first_name1 = full_name[0]
first_name2 = full_name[0:5]  # same as first_name3 below, shorthand form below
first_name3 = full_name[:5]

last_name = full_name[6:]

usr_name = full_name[::2]  # print every 2nd letter

reversed_name = full_name[::-1]

print(first_name1)
print(first_name2)
print(first_name3)
print(last_name)
print(usr_name)
print(reversed_name)

# using slice() fxn

website1 = 'http://google.com'
website2 = 'http://facebook.com'

slice = slice(7, -4)  # separate arguments with , instead of : as in indexing, slice object is reusable

print(website1[slice])
print(website2[slice])

# TOPIC: if statement = a block of code that will execute if its condition is true

# age = int(input('What is your age?: '))

# if age == 100:
#    print('Centurion!')
# elif age >= 18:
#    print('You are an Adult!')
# elif age < 0:
#   print('Unborn Person')
# else:
#   print('You are a child')

# TOPIC: logical operators (and,or) = used to check if two or more conditional statements are true.
# (not) can be used to flip the conditional statements

# temp = int(input('What is the temperature outside?: '))

# if temp >= 0 and temp <= 30:
# print('feels okay for a picnic!')
# print('Go outside!')
# elif temp < 0 or temp > 30:
# print("That's not a good feel")
# print('Stay inside!')

# TOPIC: while loop = a statement that will execute it's block of code,
#               as long as it's condition remains true

# example of infinite loop below

# while 1 == 1:
#    print("Help! I'm stuck in a loop")

# name1 = ''                               # could also use 'name = None'

# while len(name1) == 0:                   # could also use 'while not name:'
#    name1 = input('Enter Your Name: ')

# print('Hello '+name)

# TOPIC: for loop = a statement that will execute its block of code
#                    a limited amount of time

for index in range(10):
    print(index)

for i in range(50, 100):
    print(i)

for i in range(50, 100+1, 2):
    print(i)

for i in 'David Adewale':
    print(i)

# import time module at beginning of file

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)

print('Happy New Year!')

# TOPIC: Nested Loop = The 'Inner loop' will finish all of it's iterations before
#                       finishing one iteration of the 'outer loop'

rows = int(input('How many Rows?: '))
columns = int(input('How many Columns?: '))
symbol = input('What Symbol to use?: ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()
