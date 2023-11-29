#1
#Write code that concatenates two lists together without using the + sign.
l1 = [3,4,5]
l2 = [6,7,8]
l_sum = l1
for i in range(len(l2)):
    l_sum.append(l2[i])
print(l_sum)

#2
#Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for i in range(1500,2501):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end = ", ")
print()

#3
#Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

s = input("What is your name?: ")
if s in names:
    print(names.index(s))

#4
#Ask the user for 3 numbers and print the greatest number.
s = [None,None,None]
n = ["1st", "2nd", "3rd"]
for i in range(3):
    s[i] = int(input(f"Input the {n[i]} number:"))
print("The greatest number is:", max(s))

#5
#Create a string of all the letters in the alphabet
#Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for x in alp:
    if x in "AYEUIO":
        print(x, " - lowel")
    else:
        print(x, " - consonant")

#6
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
words = []
for i in range (7):
    words.append(input(f"Write the word #{i+1}: "))
print(words)

letter = input("Write a letter: ")

flag = True
for s in words:
    if letter in s:
        if flag:
            print("letter in index: ", words.index(s))
            flag = False
    else:
        print("No letter", letter, "in word -", s)

#7
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. 
# Use the sum() function to see how quickly Python can add a million numbers.
s = list(range(1,1000001))
if s[-1] == max(s) and s[0] == min(s):
    print("List is ok")
print("Sum of the list elements =", sum(s))

#8
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98

s = input("Write comma-separated numbers:")
s = "34,67,55,33,12,98"

slist = []
st = ""
for i in range(len(s)):
    
    if s[i] != ",":
        st += s[i]
    else:
        slist.append(st)
        print(st)
        st = ""
slist.append(st)
stuple = tuple(slist)
print("List:", slist)
print("Tuple:", stuple)


#9

# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

import random
nuser = (input("Write number between 1 and 9 (or 'quit' to fihish): "))
s_win = 0
s_lose = 0
while nuser != "quit":
    nrand = int(random.randint(1,9))
    print(nrand)
    if int(nuser) == nrand:
        print("Winner")
        s_win+=1
    else:
        print("Better luck next time")
        s_lose +=1
    print(f"Total {s_win} wins and {s_lose} loses")
    nuser = (input("Write number between 1 and 9: "))
 

