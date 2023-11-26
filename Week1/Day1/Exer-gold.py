#1
print ("Hello world \n"*4, "I love python \n"*4, sep="")

#2
month = int(input("What month (from 1 to 12)"))
if 3 <= month <= 5:
    print("Spring time!")
elif 6 <= month <= 8:
    print("Summer time!")
elif 9 <= month <= 11:
    print("Autumn time!")
else:
    print("Winter time!")
    