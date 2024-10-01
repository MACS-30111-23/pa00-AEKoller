# This file is intentionally empty
#
# add your code for printing out a message, such as 'Hello World!' or something else!
# print("Hello World!")
# name = input("What is your name?\n")
# print(f"Your name is {name}")

msg = f"The value of pi is {3.1415}"
print(msg)

msg = f"The value of pi is " + str(3.1415)
print(msg)

x = input("Please enter a number:\n")
y = input("Please enter a number:\n")

def addition(x, y):
    product = x + y
    return product

def subtraction(x, y):
    product = x - y
    return product

def multiplication(x, y):
    product = x * y
    return product

def division(x, y):
    product = x / y
    return product

year = 2024
if year % 4 == 0:
    print("TRUE")

year = 400
if year % 4 == 0 and year % 100 != 0:
    print("True")

if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
    print("True")

# Can also use:
year % 4 == 0 and year % 100 != 0 and year % 400 != 0