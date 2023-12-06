#1 Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def __str__(self) -> str:
        if self.currency == "dollar":
            x = f"{str(self.amount)} dollars"
        elif  self.currency == "shekel":
            x = f"{str(self.amount)} shekels"
        return x
    def __int__(self):
        x = int(self.amount)
        return x
    def __repr__(self):
        return repr(str(self))
    
    def __add__(self, n):
        if type(n) == int:
            x = self.amount + n
        elif self.currency == n.currency:
            x = self.amount + n.amount
        else: 
            raise TypeError ("Cannot add between Currency")
        return x

    def __iadd__(self, n):
        if type(n) == int:
            self.amount = self.amount + n
        elif self.currency == n.currency:
            self.amount = self.amount + n.amount
        else: 
            raise TypeError ("Cannot add between Currency")
        return self
       

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10
# print(type(c1))
# print(type(c2))
print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>




#3 Exercise 3: String Module

import string
import random

s = ""
for i in range(5):
    s += string.ascii_letters[random.randint(0,51)]
print(s)


#4 🌟 Exercise 4 : Current Date
import datetime

def currenttime():
    return datetime.datetime.now()

print(currenttime())

#5  Amount Of Time Left Until January 1st

def timeUntilSanta():
    return f"the 1st of January is in {datetime.datetime(2023, 12, 31) - datetime.datetime.now()}"

print(timeUntilSanta())

#6 Exercise 6 : Birthday And Minutes
def lifeminutes(*birthday):
    d = datetime.datetime.now() - datetime.datetime(*birthday)
    
    return d.days*24*60

s_y = int(input("Write your birth year (YYYY)"))
s_m = int(input("Write your birth month (MM)"))
s_d = int(input("Write your birth day (DD)"))

print("You lived", lifeminutes(s_y, s_m,s_d), "min")
# Create a function that accepts a birthdate as an argument (in the format of your choice), 
# then displays a message stating how many minutes the user lived in his life.

#7 Faker Module
from faker import Faker
fake = Faker()
print(fake.date())
