#1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.

number = int(input("Write the number: "))
lenght = int(input("Write the lenght: "))

list1 = []
for i in range(lenght):
    list1.append(number+i*number)
print(list1)


#2
#Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

word = input("Write the word: ")
i = 0
word2 = word[0]
for i in range(1,len(word)):
    if word[i] != word[i-1]:
        word2 = word2+word[i]
print(word2)

