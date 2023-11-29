#1
from math import sqrt
s = input("Write numbers:")
s = "100,150,180"
s = s.split(",")

for x in s:
    print(int(sqrt(2 * 50 * int(x)/30)), end =",")
print()

#2
s = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
s_list = ",".join(str(element) for element in s)
print("1. List", s_list)

s.sort(reverse=True)
s_list = ",".join(str(element) for element in s)
print("In order:", s_list)

print("Sum:", sum(s))

s_new=[]
s_new.extend ([s[0],s[-1]])
print("First, Last :", s_new)

print("Greater than 50:")
for x in s:
    if x > 50:
        print(x, end = ",")
print()

print("Smaller than 10:")
for x in s:
    if x < 10:
        print(x, end = ",")
print()

print("Sqrt:")
for x in s:
    print(x*x, end = ",")
print()




