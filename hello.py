# # variables
# name="godswill"
# age= 40
# height = 3.3
# is_logged = True
# is_Admin = False

# # how to display on terminal
# print(name, age, height)

# # type
# print(type(name))
# print(type(age))
# print(type(height))

# # concatenation with using 'f' = formated string
# first_name= 'uchenna'
# last_name ='Godswill'
# age = 22

# full_name = first_name + " " + last_name

# print(f"my name is {full_name} and i am {22} years old")

# # learning input
# name = input('enter student name: ')
# print(type(name))

# # type conversion int() for integer, float() for float,str() for string 
# age = int(input("enter age here: "))
# print(type(age))

# # basic arithemetic
# calculate = 10 + 6
# calculate2 = 10 - 6
# calculate3 = 10 * 6
# calculate4 = 10 / 2
# calculate5 = 10 % 6
# print(calculate, calculate2, calculate3, calculate4, calculate5)

# # run a mini project (birthday cal)
# birth_year = int(input('date of birth: '))
# current_year = 2025

# age = current_year - birth_year
# print(f"i am just {age} years")

# mini project 2
# amount = float(input('enter amount: '))
# dollar_rate = 1300

# naria_amount =  amount / dollar_rate
# print(naria_amount)

# mini project 3
# name = input("Enter your name: ")
# department = input("Enter department: ")
# level = input("Enter level: ")

# print('Student details')
# print(f'name: {name}')
# print(f'department: {department}')
# print(f'level: {level}')
# print(f'student detailed summary: {name}, {department},{level}')

# ASSIGNMENT
# name = input('enter your name here : ')
# age = input('enter your correct age: ')
# course = input('enter course here: ')

# print(f"welcome {name}")
# print(f"your are {age} years old")
# print(f"you study {course}")

# ass 2
# first_number = 10
# second_number = 5

# calculate = first_number + second_number
# calculatesub = first_number - second_number
# calculatemul = first_number * second_number
# calculatediv = first_number / second_number
# print(f'addition {calculate}')
# print(f'sub {calculatesub}')
# print(f'multply {calculatemul}')
# print(f'div {calculatediv}')

# ass 3
# salary = float(input('salary for the month: '))
# year = 12

# annual_salary = salary * year

# print(f'your annual salary is {annual_salary}')

# learning how to use end=""
# print("Hello World!", end=" ")
# print("I will print on the same line.")

# to make a multi line commrnt you use 
# """

# """

#global variables
# x ='awesome '
# def myFunc():
#     print(f"python is " + x)

# myFunc()

# x = 'awesome'
# count = 0

# def myfunc ():
#     global count
#     if count < 10:
#         print(f"python is " + x)
#         count += 1
#         myfunc()

# myfunc()

# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# thisList = ["apple", "banana", "cherry"]
# print(len(thisList))

# thislist = list ((1, 2, 3, 4, 5, 6, 7, 8))
# alpha = list(("a", "b", "c", "d"))

# print(thislist)
# print(thislist[1:6])
# if 1 in thislist:
#   print(f"yes we have {thislist[0]} in the list of number")

# changing things in a list
# thislist[3] = 90
# print(thislist)

# adding things in a list
# thislist.append(1000)
# print(thislist)

# to add a list to a list
# thislist.extend(alpha)
# print(thislist)

# to add from front
# thislist.insert(0, 20)
# print(thislist)

# removing
# thislist.remove(20)
# print(thislist)

# thislist.pop(0)
# print(thislist)

# del can delete the entire list and also delete a specific item
# del thislist[0]
# print(thislist)

# this will delete the entire list "del thislist"
# this will empty the list thislist.clear()

thislist = ["apple", "coconut", "cherry"]
# for x in thislist:
#     print(x)

for i in range(len(thislist)):
    print(thislist[i])    