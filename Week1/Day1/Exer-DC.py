#1

st = str(input("Write text: "))
if len(st) > 10:
    print("string not long enough")
elif len(st) < 10:
    print("string too long")
else:
    print("perfect string")

#2

print(st[0]) 
print(st[len(st)-1])   

#3
st1 = st
for i in range (0, len(st1)+1):
     print(st1[0:i])

#4
import random
x = list(st)

random.shuffle(x)
for i in x:
    print(i, end = "")
print()

