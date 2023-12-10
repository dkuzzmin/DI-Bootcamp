# import requests


#1
#       What is a class?
# It is a template to create an objects in python
#       What is an instance?
# It is object created from a class
#       What is encapsulation?
# It is way to store some methos only inside the class
#       What is abstraction?
#eehhh
#       What is inheritance?
# It is class inside class
#       What is multiple inheritance?
# It is some class inside one parent class 
#       What is polymorphism?
#Eeeehh
#       What is method resolution order or MRO?
#I need to learn :)



#2
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.deck = self.make_desk()
        # self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        # self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        # self.suits = suits
        # self.values = values  
    def make_desk(self):
        deck1 = []
        suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for suit in suit_list:
            for value in values_list:
                card = f"{value} of {suit}"
                deck1.append(Card(suit, value))
        return deck1
    
    def shuffle(self):
        s_desk = random.sample(self.deck, 52)
        return s_desk
    
    def deal(self):
        return self.deck.pop()


x = Deck()
print(x.shuffle())




deck = Deck()
deck.shuffle()
card = deck.deal()
if card:
    print(f"You have dealt: {card.value} of {card.suit}")
else:
    print("No more cards in the deck.")