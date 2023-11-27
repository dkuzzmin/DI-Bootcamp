
#find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

list1 = [5, 10, 15, 20, 25, 50, 20]

list1[list1.index(20)] = 200
print(list1)



#Accept a number from the user and print its multiplication table
n = int(input("Number?:  "))
for i in range(10):
    print(n,"*",i+1,"=",n*(i+1))

#Print the numbers from 1 to 10 using while loop

n = 1
while n < 11:
    print(n)
    n += 1