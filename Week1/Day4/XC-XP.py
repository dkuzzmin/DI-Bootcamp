#1
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

def display_message():
    print("We are learning Python")


display_message()


#2
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("World and Peace")

#3
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(city, country="Israel"):
    print(f"“{city} is in {country}”")

describe_city("Kazan")

#4
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random

def rndm(n):
    n2 = random.randint(1,100)
    if n == n2:
        print("Success")
    else:
        print(f"Fail: {n} and {n2}")

# check = "a"
# while not check.isdigit():
#     check = input("Write number (1 to 100):")
#print(check)


rndm(100)


#5
def make_shirt():









    