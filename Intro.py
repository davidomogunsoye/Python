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

age = int(input('What is your age?: '))

if age == 100:
    print('Centurion!')
elif age >= 18:
    print('You are an Adult!')
elif age < 0:
   print('Unborn Person')
else:
    print('You are a child')

# TOPIC: logical operators (and, or) = used to check if two or more conditional statements are true.
# (not) can be used to flip the conditional statements

temp = int(input('What is the temperature outside?: '))

if temp >= 0 and temp <= 30:
    print('feels okay for a picnic!')
    print('Go outside!')
elif temp < 0 or temp > 30:
    print("That's not a good feel")
    print('Stay inside!')

# TOPIC: while loop = a statement that will execute its block of code,
#               as long as it's condition remains true

# example of infinite loop below

#while 1 == 1:
#   print("Help! I'm stuck in a loop")

name1 = ''                               # could also use 'name = None'

while len(name1) == 0:                   # could also use 'while not name:'
        name1 = input('Enter Your Name: ')

print('Hello '+name)

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


# TOPIC: loop control statements = change the execution of a loop from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop. can be used to skip certain characters
# pass = does nothing, acts as a placeholder

while True:
    name = input('What is your name?: ')
    if name != '':
        break

phone_number = '123-345-345'

for i in phone_number:
    if i == '-'
    continue
   print(i, end='')

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)


# Topic: list = used to store multiple items in a single variable

food = ['pizza', 'Rice', 'Sausage', 'Noodles']

print(food)
print(food[2])

food[3] = 'Goat meat'

print(food)
print(food[3])

# To print elements in a list

for x in food:
    print(x)

food.append('Tea')      # adds a new element at the end
food.remove('Rice')     # removes a specific element
food.pop()              # removes the last element
food.insert(1, 'Pancakes')
food.sort()             # sorts elements in alphabetical order
# food.clear()            # removes all elements from list

for x in food:
    print(x)

# TOPIC: 2D Lists or multidimensional lists = a list of lists

drinks = ['Coke', 'fanta', 'pepsi', 'vodka', 'rum']
dinner = ['sandwich', 'noddles', 'Burger', 'chicken', 'spag']
dessert = ['cake', 'ice cream']

food = [drinks, dinner, dessert]

print(food)
print(food[0][2])

# TOPIC: Tuple = collection which is ordered and unchangeable
#                used to group together related data

student = ('David', 21, 'male')

print(student.count('David'))
print(student.index(21))

for x in student:
    print(x)

if 'Bro' in student:
    print('Bro is in student!')
else:
    print('Not a student!')

# TOPIC: Set = collection which is unordered, unindexed. no duplicate values

utensils = {'Forks', 'Knife', 'spoon', 'chopstick', 'spoon'}
dishes = {'plate', 'bowl', 'cup', 'Knife'}

utensils.add('napkin')
utensils.remove('spoon')
# utensils.clear()

utensils.update(dishes)  # to add a set to another set

dinner_table = utensils.union(dishes)  # to join two sets to form another set

for x in utensils:
   print(x)

for x in dinner_table:
   print(x)

print(utensils.difference(dishes))  # check what utensils have that dishes doesn't

print(utensils.intersection(dishes))  # check what elements they have in common

# TOPIC: dictionary = A changeable, unordered collection of unique key: value pairs
#                     fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

print(capitals['Russia'])

print(capitals.get('Germany'))  # safe way of checking if there is a key

print(capitals.keys())  # print all available keys

print(capitals.values())  # print all available values

print(capitals.items())  # print dictionary

capitals.update({'Germany': 'Berlin'})  # add new key:value pair

capitals.update({'USA': 'Las Vegas'})  # update an existing key:value pair

capitals.pop('China')  # remove specified key

for key, value in capitals.items():
    print(key, value)        # alternative method of printing dictionary

# TOPIC: Index operator [] = gives access to a sequence's element (str, list, tuples)

name = 'david Adewale'
first_name = name[:5].upper()
last_name = name[6:].capitalize()
last_character = name[-1]

if name[0].islower():
    name = name.capitalize()

print(name)
print(first_name)
print(last_name)
print(last_character)

# TOPIC: function = a block of code which is executed only when it is called


def hello(name, last_name, age):  # parameters in () need to match the number of arguments
    print('Hello ' + name + ' ' + last_name)
    print('you are ' + str(age) + ' years old')
    print('Have a nice day!')


hello('David', 'Adewale', 25)  # function with arguments passed, these are positional arguments meaning order matters

# TOPIC: Return statement = functions send python values/objects back to the caller.
#                            these values/objects are known as the function's return value


def multiply(number1, number2):
    result = number1 * number2
    return result


print(multiply(6, 8))

# or store within a variable

x = multiply(5, 6)

print(x)

# or to use fewer code lines


def multiply2(number3, number4):
    return number3 * number4


y = multiply2(7, 9)

print(y)

# TOPIC: keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     python knows the names of the arguments that our function receives

def hello(first, middle, last):
    print('Hello'+' '+first+' '+middle+' '+last)


hello(last='Adewale', middle='Om', first='David')  # order of arguments don't matter as long as they have the keyword
hello(middle='Om', last='Adewale', first='David')

# TOPIC: nested functions calls = function calls inside other function calls
#                                 innermost function calls are resolved first
#                                 returned value is used as argument for the next outer function

num = input('Enter a whole positive number: ')
num = float(num)
num = abs(num)
num = round(num)
print(num)

# or can be written with one line of nested functions

print(round(abs(float(input('Enter a whole positive number: ')))))






