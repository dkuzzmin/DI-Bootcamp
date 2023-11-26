#1
print("Hello world \n"*4)

#2
res = (99**3)*8
print(res)

#3
print(False)
print(True)
print(False)
print(False)
print(False)

#4
computer_brand = "MacBook"
print(f"I have a {computer_brand} computer")

#5
name = "Dima"
age = 40
shoe_size = 11
info = f"{name} live in Israel, he is {age} and have {shoe_size} size"
print (info)

#6
a = 5
b = 3
if a > b:
    print("Hello world")

#7
n = int(input("Enter the number: "))
if n%2 == 0:
    print(n, "is odd")
else:
    print(n, "is even")

#8
s = input("Your name is:")
if s == name:
    print(f"Hi buddy, {s}")

#9
user_h = int(input("you height is (in inches):"))
if user_h > 145/2.54:
    print("You are enough tall to ride")
else:
    print("You need to grow more") 