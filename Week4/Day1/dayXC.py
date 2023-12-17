

# 0 tax on income below 10,000, 
# 5% tax on income from 10,000 to 15,000, 
# 10% tax on income above 15,000

# user_income = int(input("Write Your income: "))

# if user_income < 10000:
#     tax = 0
# elif user_income >= 15000:
#     tax = user_income * 0.1
# else:
#     tax = user_income * 0.05

# print(f"Your tax is {tax}") 




# 1. Write code that gets three words from a user and inputs them into a sentence using
# F-Strings.
s1 = input("Write 1 word: ")
s2 = input("Write 2 word: ")
s3 = input("Write 3 word: ")
print(f"{s1}, {s2}, {s3}")

# 2. Exercise: Write a list that contains 2 strings. Print the second string in uppercase and
# then the first string backwards.
s = ["Hello", "Goodbay"]
print(s[0].upper())
print(s[1][::-1])

# 3. Write code for a list that contains four names and prints every other name.
s = ["Bill", "Andy", "Jimmy", "Antony"]
for i in range(4):
    print(s[i])

# 4. Write code for a list of numbers. Ask a user for a new number and insert it into the list,
# second from the end.
n = [1,2,3,4,5]
n1 = int(input("Write a number: "))
n_new = n[:-1]
n_new.append(n1)
n_new.append(n[-1])
print(n_new)    
# 5. Exercise: Create a dictionary containing the following information about you: your name,
# your age, your gender, your favorite food. Be sure to use appropriate keys.
me = {
    'Name' : 'Dima',
    'Age' : 40,
    'Gender' : 'Male',
    'Favorite food' : 'Pizza'
}

# 6. Exercise: A user is allowed to drive home if their blood alcohol is less than 0.5 %. Ask a
# user for their blood alcohol level and if they're not sober, tell them to take a cab.
blood = float(input("Enter you blood alcohol test: "))
if blood >= 0.5:
    print("Take a cab")
else:
    print("Allowed to drive")

# 7. Exercise: If a user is male and over 65 or female and over 60, they may retire. Get a
# gender and age from the user and let them know if it's time to retire.
gender = input("Write your gender ('Male' or 'Female'): ")
age = int(input("How old are you: "))
if (age > 65 and gender.upper() == "MALE") or (age > 60 and gender.upper() == "FEMALE"):
    print("You may retire")

# Loops
# 8. Exercise: Write a loop to print every number between 10 and 20.
# 9. Exercise: Write a loop to print every odd number between 1 and 20.
# 10. Exercise: Write code with a list of five names. Print the names one by one using a loop.
# 11. Exercise: Write a loop that takes numbers from the user until it receives the number 0
# and prints the sum of the numbers received.
# 12. Exercise: Write a loop that takes words from the user until it receives the word 'done' and
# prints the longest word received.
# Functions
# 13. Exercise: Write a function that takes a string as input and prints its length:
# 14. Exercise: Define a function that takes three numbers and prints their average.
# 15. Exercise: Define a function that takes two arguments, a string and a number and checks
# if the string has more characters than the number. Example: 'string', 3 prints True since
# string has 5 characters.
# 16. Exercise: Write a function that copies a string a certain number of times, based on the
# input. Set the default amount of copies to be 1.