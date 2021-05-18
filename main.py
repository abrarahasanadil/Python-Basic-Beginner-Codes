from time import sleep
from threading import *
import threading
import mysql.connector as connector
import math
import os
import random
from pathlib import Path

# * IMPORTS THE ENTIRE CONVERTER MODULE
import converter
# * IMPORTS THE ENTIRE CONVERTER MODULE FROM PACKAGE
import ecommerce.shipping
from converter import lbs_to_kg  # * IMPORTS SPECIFIED MODULE
# * IMPORTS SPECIFIED MODULE FROM PACKAGE
from ecommerce.shipping import calc_shipping
from utils import find_max

print("Let's learn Python")

# !--------------------------------------------------VARIABLES
x = 10000
print(x)
haire_py = False
print(haire_py)

# !----------------------------------------------TAKING INPUT
name = input("Who am I speeking to?")
color = input("Which color do you like?")
print(name + " likes " + color)

# !----------------------------------------------TYPE CONVERSION
birth_year = input("Birth year: ")
print(type(birth_year))
age = 2020 - int(birth_year)
print(type(age))
print(age)

# !----------------------------------------------STRINGS
email = """
Hey Nazi,
you know I am your "HUBBY"
Abrar
"""
print(email)
name = "Abrar lala bhai"
print(name[6])
print(name[0:6])
name_copy = name[:]
print(name_copy)

# !----------------------------------------------FORMATTED STRINGS
name = "Abrar"
surname = "Chowdhury"
output1 = name + " [" + surname + "] is a legend"
output2 = f"{name} {surname} is a legend"
output3 = f"{surname}s' are known as the most important family for Bangladesh"
print(output1)
print(output3)

# !----------------------------------------------CALC CHAR
name = "Dor  aemon"
print(len(name))
name = "Doraemon"
print(len(name))

# !----------------------------------------------UPPER/LOWER CHAR
wife = "nazia"
print(wife.upper())
hubb = "ABRAR"
print(hubb.lower())

# !----------------------------------------------REPLACE/IN/FIND CHAR
statement = "Nazia amr Gudugudu Baby"
print(statement)
print("WAIT NO NO NO")
print(statement.replace("Baby", "Jaaner Tukra Babe"))
print("Nazia" in statement)
print(statement.find("gudugudu"))
print(statement.find("Gudugudu"))

# !----------------------------------------------INT DIVISION/EXPONENT
print(19239 // 332)
print(2 ** 2)

# !----------------------------------------------MATH FUNC

x = 33.53
print(round(x))
print(int(x))
print(x * -1)
print(abs(x))
print(math.log(x))
print(math.log(x, 33.53))
print(int(math.log(x, 33.53)))

# !----------------------------------------------CONDITION STATEMENT
is_sexy = False
is_ugly = True

if is_sexy:
    print("Abrar is Sexy")
    print("Nazia loves him")
elif is_ugly:
    print("Abrar is ugly as f*ck")
    print("Nazia still will marry him")
else:
    print("Whatever Abrar looks like doesn't matter")
    print("Nazia will always fucking marry Abrar")
print("Alhamdulillah Nazi still will be beside")
print("Good Night")

# !----------------------------------------------AND/OR/NOT OPERATORS
has_high_incomes = True
has_criminal_record = True

if has_high_incomes and not has_criminal_record:
    print("Eligible on Loan")
else:
    print("Bair ho beda")

# !----------------------------------------------COMPARISONS
temperature = 20

if temperature > 30:
    print("It's a HOT day")
elif temperature <= 10:
    print("It's a COLD day")
else:
    print("Natishitoshno")

name = input("Please Enter Your Name, Sir")
check = len(name)

if check < 3:
    print("Name should be at least 3 characters")
elif check > 50:
    print("Name should be maximum of 50 characters")
else:
    print("Name looks good!!!")

weight = input("Sir would you please enter your weight? ")
unit = input("(L)lbs or (K)kg: ")

if unit.upper() == "L":
    print(float(weight) * 0.45)
if unit.upper() == "K":
    print(float(weight) / 0.45)

# !----------------------------------------------WHILE LOOP
# ? EXECUTE A BLOCK OF CODES MULTIPLE TIMES

i = 5
while i >= 1:
    print("*" * i)
    i = i - 1
print("done")

# !----------------------------------------------GUESSING GAME
secret_number = 9
guess_count = 1
guess_limit = 3
while guess_count <= guess_limit:
    check = input("GUESS: ")
    guess_count += 1
    if int(check) == secret_number:
        print("You Win!!!")
        break
else:
    print("You lost :'(")

# !----------------------------------------------CAR GAME
command = ""
started = False

while command != "quit":
    command = input(">>> ").lower()
    if command == "start":
        if started:
            print("Already started")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print(
            """
Start - Starts the car
Stop - Stops the car
Quit - End Game
       """
        )
    else:
        print("Unknown command")
else:
    print("Game Ended")

# !----------------------------------------------FOR LOOP
# ? ITERATE OVER ITEMS OF A COLLECTION

for item in "Python":
    print(item)
print("*" * 10)
for item in ["Abrar", "Nazia", "Chowdhury"]:
    print(item)
print("*" * 10)
for item in [0, 1, 2, 3]:
    print(item)
print("*" * 10)
for item in range(10):
    print(item)
print("*" * 10)
for item in range(5, 10):
    print(item)
print("*" * 10)
for item in range(5, 10, 2):
    print(item)
print("*" * 10)

total = 0

for price in [10, 20, 30]:
    total += price
print(f"So the price is {total}$")

# !----------------------------------------------NESTED LOOPS
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

for i in [5, 2, 5, 2, 2]:
    print("X" * i)

numbers = [2, 2, 2, 2, 5]

for i in numbers:
    output = ""
    for j in range(i):
        output += "x"
    print(output)

# !----------------------------------------------LISTS
names = ["lallu", "mallu", "kallu", "hallu", "tallu", "ballu", "gallu"]
print(names)
print(names[0])
print(names[1:])
print(names[-1])
names[5] = "jallu"
print(names)
print(names[:6])

# !----------------------------------------------MAXIMUM IN A LIST
names = [
    "aaaaa",
    "ac",
    "a",
    "asaaac",
    "aaddda",
    "afbd",
    "cc",
    "eaaaaaaaaa",
    "ba",
    "m",
    "qsscfsaa",
    "bvdffdAa",
    "rcts",
]

max = names[0]
sec = names[0]
count = 1
index = 0
index2 = 0

for i in range(1, len(names)):
    if len(max) > len(names[i]):
        max = max
    elif len(max) == len(names[i]):
        if count >= 2:
            sec = sec
        else:
            sec = names[i]
            index2 = i
        count += 1
    elif len(max) < len(names[i]):
        max = names[i]
        index = i
        if len(str(sec)) < len(names[i]):
            sec = len(names[i])
        count = 1

if count == 1:
    print(
        f"there is only {count} maximum which is {max} with lenght {len(max)} in {index} of names"
    )
else:
    print(
        f"""There are {count} maximums with same number of alphabets among which first two are:

   First maximum is {max} of length {len(max)} which is in the index {index} of names
   and
   Second maximum is {sec} of length {len(sec)} which is in the index {index2} of names"""
    )

largest = None
smallest = None
sval = None


def lnum(i, largest):
    if largest is None:
        largest = i
    elif i > largest:
        largest = i
    return largest


def snum(i, smallest):
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
    return smallest


while True:
    sval = input("Enter a Number: ").upper()

    if sval == "DONE":
        break
    try:
        ival = int(sval)
    except:
        print("Invalid Input")
        continue

    largest = lnum(ival, largest)
    smallest = snum(ival, smallest)

print("Maximum is", largest)
print("Minimum is", smallest)

# !----------------------------------------------2D LISTS
# ? 2D LIST IS A LIST WHERE ITEMS INSIDE THE LIST ARE INDIVIDUAL LISTS

# Given matrix
#     1  2  3                                    # * 1st list having 3 items
#     4  5  6                                    # * 2nd list having 3 items
#     7  8  9                                    # * 3rd list having 3 items

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for item in row:
        print(item)

for row in matrix:
    print(row)

print(matrix)
print(matrix[0])
print(matrix[0][1])
print(matrix[0][1])

# !----------------------------------------------LIST METHODS
numbers = [9, 5, 3, 2, 5, 8]

# ? APPEND
numbers.append(10)
print(numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7]

for i in range(8, 21):
    numbers.append(i)

print(numbers)

# ? INSERT
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
numbers.insert(6, 'hello')
print(numbers)

# ? REMOVE
numbers = [5, 0, 1, 2, 3, 4, 5, 6, 7, 5]
numbers.remove(5)
# * Does the first 5 it finds not all
print(numbers)

# ? POP
numbers = [0, 1, 2, 3, 4, 90, 6, 7]
# * Pops the given index not the value
numbers.pop(5)
print(numbers)
numbers.pop()
print(numbers)

# ? INDEX AND CHECKING
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
print(numbers.index(5))
print(50 in numbers)

# ? COUNT
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 2, 2, 4, 6]
print(numbers.count(2))

# ? SORT AND REVERSE
numbers = [0, 1, 2, 5, 50, 1000, 3, 4, 5, 6, 7]
print(numbers.sort())                            # * Returns 'None'
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

# ? COPY
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
numbers2 = numbers.copy()
numbers.append(8)
print(numbers)
print(numbers2)

# ? CLEAR
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
numbers.clear()
print(numbers)

# !----------------------------------------------REMOVING DUPLICATES
numbers = [0, 9, 5, 3, 2, 5, 8, 4]

new_number = []

for i in numbers:
    if i not in new_number:
        new_number.append(i)
print(new_number)

# !----------------------------------------------PRINTING MULTIPLES


def solution(number):
    x = []
    for num in range(1, number):
        x.append(num)
    print(x)

    count = 0

    for i in x:
        if i % 3 == 0:
            count = count + i
        elif i % 5 == 0:
            if i % 3 == 0:
                pass
            count = count + i

    return count


solution(23)

# !----------------------------------------------TUPLES
# ? UNLIKE LIST CAN'T BE MODIFIED

tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple[:9])


# !----------------------------------------------UNPACKING
coordinates1 = (10, 20, 30, 40)

x = coordinates1[0]
y = coordinates1[1]
Z = coordinates1[2]
print(x)

# OR
coordinates2 = (100, 200, 300, 400)
a, b, c, d = coordinates2
print(d)

# !----------------------------------------------DICTIONARIES
# ? INTRODUCE BY USING CURLY BRACES

customer = {
    "name": "Abrar",
    "age": 21,
    "is_verified": True
}

print(customer.get("name"))
print(customer.get("birthdate"))
customer.get("address", "North Khulshi Hills, Chittagong, Bangladesh")
customer["birthdate"] = "15th July 2000"
print(customer.get("birthdate"))

output = ""
numbers = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five"}

phone = input("Phone: ")

for char in phone:
    output += numbers.get(char, "!") + " "
print(output)

# ? EMOJI CONVERTER
message = input("> ")
words = message.split(" ")
print(words)
emoji = {":)": "😊", ":(": "😞"}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)

phonebook = {
    "nazia": ["01305981601", "nazia@gmail.com"],
    "ammu": ["01684130126", "shaheen@gmail.com"],
}
print(phonebook["nazia"][0])

# !----------------------------------------------FUNCTIONS


def greet_user():
    print("Hello")


print("Start")
greet_user()
print("Finish")

# ? PARAMETERS


def greet_sir(i, j):
    name = i
    prof = j
    print(
        f"""
   Hello Mr. {name}, our {prof},
   Welcome aboard
   """
    )


greet_sir(input("Your Name Sir: "), input("Your Position Sir: "))

# !----------------------------------------------RETURN STATEMENT


def square(number):
    return number * number


output = (1000 * square(2)) + (
    square(int(input("Enter which number you would like to square: "))) / 4
)
print(output)

# ? EMOJI CONVERTER USING FUNCTIONS


def emo_conv(message):
    words = message.split(" ")
    emoji = {":)": "😊", ":(": "😞"}
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input("> ")
print(emo_conv(message))

# !----------------------------------------------EXCEPTIONS
try:
    age = int(input("Age: "))
    income = 50000
    risk = income / age
    print(risk)
except ValueError:
    print("Please enter a valid age")
except ZeroDivisionError:
    print("Can't use zero as an age")

# !----------------------------------------------CLASSES & CONSTRUCTORS
# ? USED TO DEFINE NEW TYPES
# ? A FUNCTION WHICH GETS CALLED DURING OBJECT CREATION

# * FUNCTIONS


class Student:
    def study(self):
        print(
            f"""
Hi I am {self.name} and I am studying
       """
        )

    def draw(self):
        print(
            f"""
Hey I am {self.name} just drawing
       """
        )

# * CONSTRUCTORS
    def __init__(self, name, age, section):
        self.name = name
        self.age = age
        self.section = section


# ? OBJECT IS AN INSTANCE OF A CLASS
# ? CLASS DEFINES THE TEMPLATE FOR CREATING OBJECT


# ? OBJECT CREATION
student1 = Student("Abrar Chowdhury", 21, "Hufflepuff")
student2 = Student("Nazia Rahman", 16, "Loonitunes")
print(student1)
print(id(student1))
student1.study()
print(student1.name)
print(student1.age)
print(student1.section)
print("*" * 100)

student2.draw()
Student.draw(student2)

print(student2.name)
print(student2.age)
print(student2.section)

# !----------------------------------------------INHERITENCE
# ? CHILDREN CLASS INHERIT ATTRIBUTES FROM PARENT CLASS


class Mom:
    def blue_eyes(self):
        print("I have got Blue Eyes")


class Son(Mom):
    pass


abrar = Son()
abrar.blue_eyes()

# !----------------------------------------------MODULES
# ? BASICALLY A FILE WITH PYTHON CODE AND USED TO ORGANIZE MULTIPLE FILES
# ? A FILE UNDER MAIN FOLDER CREATED FOR WEIGHT CONVERSION

converter.kg_to_lbs(81)

lbs_to_kg(180)

# ? FIND MAX USING MODULES
numbers = [4, 50, 6, 1, 800, 3, 10, 2, 29]
print(find_max(numbers))

# !----------------------------------------------PACKAGES
# ? WAY OF ORGANIZING RELATED MODULES UNDER SAME PACKAGES
# ? A FOLDER/PACKAGE UNDER THE PROJECT CREATED WHERE MODULES ARE ORGANIZED

ecommerce.shipping.calc_shipping(7)

calc_shipping(7)

# !----------------------------------------------GENERATING RANDOM VARIABLES
# ? GOOGLE 'PYTHON 3 MODULE INDEX' TO ACCESS ALL BUILT-IN MODULE

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))
    print(random.randrange(5, 8))

# ? WHO WON THE GRAMMY?
songs = {
    "BACK TO HOME": "Who We Are",
    "BILLIE EILISH": "Bad Guy",
    "SHAWN MENDES": "Wonder",
    "BTS": "Dynamite",
    "THE WEEKND": "Blinding lights",
}
print(
    f"""
The nominees of 63rd Annual Grammy Awards are:
"""
)

members = ["Back to Home", "Billie Eilish",
           "Shawn Mendes", "BTS", "The Weeknd"]
for member in members:
    print(member)

winner = random.choice(members).upper()
song_name = songs.get(winner)
print(
    f"""
This year the Grammy Award goes to.............
{winner} for the song "{song_name}"
"""
)

# ? ROLL THE DICE
command = ""
while command != "QUIT":
    command = input(
        "Press enter to roll or 'quit' to end the game >>> ").upper()
    if command == "":
        print(f"{random.randint(1, 6)}, {random.randint(1, 6)}")
    elif command == "QUIT":
        print("Game Over")
        break
    else:
        print("Invalid command")

# ? ROLL THE DICE USING CLASSES


class Dice:
    def roll(self):
        numbers = (1, 2, 3, 4, 5, 6)
        dice_roll = (random.choice(numbers), random.choice(numbers))
        return dice_roll


dice = Dice()
print(dice.roll())

# !----------------------------------------------FILES & DIRECTORIES

path = Path("ecommerce")
print(path.exists())

# ? MAKING & REMOVING DIRECTORIES
path = Path()
path.mkdir()
path.rmdir()

# ? FIND FILES OR DIRECTORIES IN A GIVEN PATH
# * SEARCHES ALL THE FILES AND DIRECTORIES
for file in path.glob("*"):
    print(file)
print("*" * 100)
for file in path.glob("*.*"):                    # * SEARCHES ONLY FILES
    print(file)
print("*" * 100)
for file in path.glob("*.py"):                   # * SEARCHES ONLY PY FILES
    print(file)
print("*" * 100)

# * RETURNS CURRENT WORKING DIRECTORY
print(os.getcwd())

print(os.getcwdb())                              # * DIRECTORY AS BYTE OBJECT

# ? OPENING FILES
new_file = open("MyInfo.txt", "r")
print(new_file.read())
new_file = open("MyInfo.txt", "w")
new_file.write(
    """Mohammed Abrar Ahasan Chowdhury
Python Developer
21
"""
)
new_file = open("MyInfo.txt", "a")
new_file.write("Musician and Song Writer and Producer")

# !----------------------------------------------PYPI & PIP
# ? DOWNLOADED OPENPYXL IN TERMINAL

# !----------------------------------------------ARRAY DIFFERENCE


def array_diff(a, b):
    for number in b:
        while number in a:
            a.remove(number)

    print(a)


array_diff([1, 2, 2, 2, 2, 4, 5, 2, 2], [2, 4])

# !----------------------------------------------FACEBOOK LIKES


def likes(names):
    if not names:
        return 'no one likes this'
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) <= 3:
        count = 0
        temp = ''
        for name in names:
            count = count + 1
            if count != len(names):
                if count != len(names) - 1:
                    temp = temp + name + ', '
                else:
                    temp = temp + name + ' '
            else:
                temp = temp + f"and {name} like this"
        return temp
    else:
        count2 = 0
        temp2 = ''
        for name in names:
            count2 = count2 + 1
            if count2 <= 2:
                if count2 == 1:
                    temp2 = temp2 + name + ', '
                else:
                    temp2 = temp2 + name + ' '
            elif count2 == len(names):
                temp2 = temp2 + f"and {count2-2} others like this"
        return temp2


likes([])
likes(['Abrar'])
likes(['Abrar', 'Nazia'])
likes(['Abrar', 'Nazia', 'Rafid'])
likes(['Abrar', 'Nazia', 'Rafid', 'Shojon'])
likes(['Abrar', 'Nazia', 'Rafid', 'Shojon', 'Shanto'])
likes(['Abrar', 'Nazia', 'Rafid', 'Shojon', 'Shanto', 'Oraib'])

# !----------------------------------------------CALCULATION IN FUNCTIONS


def five():
    y = 5
    return y


def seven(a):
    x = 7
    print(a)

    y = a

    i = 0
    temp = 0
    for j in range(a):
        while i == "(":
            temp += j

    temp(x, y)


def times(x, y):
    output = x*y
    print(output)


seven(times(five()))

# !----------------------------------------------CONNECTING A DATABASE


class DBassist:
    def __init__(self):

        # ? Creating a variable in the object which connects the code with mysql
        self.con = connector.connect(user='admin',
                                    password='Admin1234$',
                                    host='127.0.0.1',
                                    port='3306',
                                    database='bloodbank')

        # ? Firing up the query
        c = self.con.cursor()

        c.execute('''create table if not exists doctor(doctor_id char(4) primary key,
                                                        doctor_phone varchar(11),
                                                        doctor_name varchar(100))''')
        print('done')


out = DBassist()

# !----------------------------------------------THREADING


def run1():
    for i in range(1, 11):
        print(i)
        sleep(0.1)
    sleep(3)
    for i in range(21, 31):
        print(i)
        sleep(0.1)


def run2():
    for i in range(11, 21):
        print(i)
        sleep(0.1)


x = threading.Thread(target=run1)
y = threading.Thread(target=run2)


x.start()

sleep(2)

y.start()

x.join()
y.join()

print('End')
