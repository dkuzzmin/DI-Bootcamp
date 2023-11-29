#1
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

def display_message():
    return print("We are learning Python")


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
def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text is '{text}'")

def make_shirt(size="Large", text="I love python"):
    print(f"The size of the shirt is {size} and the text is '{text}'")


make_shirt("L", "TEL AVIV")
make_shirt()
make_shirt("M")
make_shirt("XS", "TEL AVIV")
user_size = "S"
user_text = "RISHON"
make_shirt(user_size, user_text)
make_shirt(size = "XL", text = "RISHON")

#6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    for x in names:
        print(x, end=", ")
    print()

show_magicians(magician_names)


def make_great(names):
    for x in names:
        print(x)
        names[names.index(x)] += " The Great"
    return names

magician_names = make_great(magician_names)

print(magician_names)

#7
#7.1
def get_random_temp():
   return random.randint(-10,40)

print(get_random_temp())

#7.2
def main():
    print(f"The temperature right now is {get_random_temp()} degrees Celsius.")

main()

#7.3
def main():
    advices = ["Brrr, that’s freezing! Wear some extra layers today",
            "Quite chilly! Don’t forget your coat",
            "Today is very comfort weather",
            "Time to go to the beach",
            "Save the skin from sun"]
    t = get_random_temp()
    print(f"The temperature right now is {t} degrees Celsius.")
    if t <= 0:
        print(advices[0])
    elif 0 < t <= 16:
        print(advices[1])
    elif 16 < t <= 23:
        print(advices[2])
    elif 24 < t <= 32:
        print(advices[3])
    elif 32 < t <= 40:
        print(advices[4])
main()

#7.4
def get_random_temp(season):
   seas = {"Summer" : (20, 40),
           "Autumn" : (10, 25),
           "Winter" : (-10, 15),
           "Sping" : (5, 30),   
   }
   temp = random.randint(*seas[season])
   return temp

print(get_random_temp("Winter"))

def main():
    advices = ["Brrr, that’s freezing! Wear some extra layers today",
            "Quite chilly! Don’t forget your coat",
            "Today is very comfort weather",
            "Time to go to the beach",
            "Save the skin from sun"]
    t = get_random_temp(input("Write Season now: "))
    print(f"The temperature right now is {t} degrees Celsius.")
    if t <= 0:
        print(advices[0])
    elif 0 < t <= 16:
        print(advices[1])
    elif 16 < t <= 23:
        print(advices[2])
    elif 24 < t <= 32:
        print(advices[3])
    elif 32 < t <= 40:
        print(advices[4])
main()

#7.5 bonus


#7.5 bonus


#8
import random
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

def starwarquiz(*args):
    data = args
    wrong_answers = list()
    correct_answers = list()
    flag = True
    rand_x = random.randint(0,len(data)-1)
    while len(correct_answers)+len(wrong_answers) < len(data):
        while rand_x in wrong_answers or rand_x in correct_answers:
            rand_x = random.randint(0,len(data)-1)
        # print(rand_x)
        print(data[rand_x]["question"])
        answer = input()
        if answer == data[rand_x]["answer"]:
            print("Exactly!")
            correct_answers.append(rand_x)
        else:
            print("No!")
            wrong_answers.append(rand_x)
    return wrong_answers, correct_answers

def usersstat(wrong:list, correct:list):
    print(f"Your stats:{int(100*len(correct)/(len(correct)+len(wrong)))}%")
    print(f"Correct answers:{len(correct)}")
    print(f"Wrong answers:{len(wrong)}")
    

usersstat(*starwarquiz(*data))