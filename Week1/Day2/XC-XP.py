#1
my_fav_numbers = {16, 20, 5, 7, 46}

my_fav_numbers.add(34)
my_fav_numbers.add(78)
print(my_fav_numbers)

my_fav_numbers.remove(78)

print(my_fav_numbers)

friend_fav_numbers = {76, 78, 20, 8, 7}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("concate:", our_fav_numbers)

#2

print("Given a tuple which value is integers, is it possible to add more integers to the tuple?")
print("No")

#3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)

# 4
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
print("Recap – What is a float? What is the difference between an integer and a float?")
print("Answer: ", "Number with floating point, not a whole number")
print("Can you think of another way to generate a sequence of floats?")
print("Answer: ", "By dividing integers by each other?")

x = list(range(3,11))
x1 = []
for i in x:
    if i%2 != 0:
        x1.append(i/2)
    else:
        x1.append(int(i/2))
print(x1)

#5

#Use a for loop to print all numbers from 1 to 20, inclusive.
#Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
for i in range(20):
   print(i+1, end=" ")
print()
for i in range(20):
    if i % 2 == 0:
        print(i+1, end=" ")
print()

#6
#Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

s = input("What is your name?")
while s != "Dima":
    s = input("What is your name?")

#7

# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

user1 = input("Write fruits (separated with a single space): ")
userlist = user1.split()
print(userlist)
#user2 = input("Write any fruit")
if input("Write any fruit: ") in userlist:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

#8

# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

toplist = []
while "quit" not in toplist:
    s = input("Enter a pizza topping: ")
    toplist.append(s)
    print("Topping is added")
toplist.remove("quit")
print(f"Your toppings are: {', '.join(toplist)}. Total price is {10+2.5*len(toplist)}")

#9
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

toplist = []
while "quit" not in toplist:
    s = input("Write the age of every person for ticket? (write 'quit' to finish)")
    toplist.append(s)
    print("Added")
toplist.remove("quit")
print(f"Your tickets for the people with ages: {', '.join(toplist)}")

sum = 0
for x in toplist:
    if int(x) >12 :
        sum = sum + 15
    elif 3 < int(x) <= 12:
        sum = sum + 10
print("Total price: $", sum)


print()


names = ["Ester", "Diana", "Anna", "Anastasia"]
xnames = names.copy()
for x in names:
    print(x)
    age = int(input(f"How old are you, {x}?"))
    if 21 > age > 16:
        xnames.remove(x)

print(f"Attendees: {', '.join(xnames)}")

#10
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# We need to prepare the orders of the clients:
    # Create an empty list called finished_sandwiches.
    # One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)

finished_sandwiches = []

while sandwich_orders != []:
    prepare = sandwich_orders.pop()
    finished_sandwiches.append(prepare)
#print("Ready kitchen: ", finished_sandwiches)
for x in finished_sandwiches:
    print("I made your", x.lower())

