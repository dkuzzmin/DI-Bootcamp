from XP2 import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, trained = False):
        self.name = name
        self.age = age
        self.trained = trained
    def train(self):
        self.bark()
        self.trained = True
        return self
    def play(self, *args):
        print(self.name, end = " ")
        for x in args:
            print(f"{x.name}", end = " ")
        print("all play together")
        return self
    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        if self.trained:
            print(f"{self.name}", tricks[random.randint(0, 3)])
        return self

dog1 = PetDog("Bobik", 23, 22)
print(dog1.name)
dog1.train()
print(dog1.trained)

dog2 = PetDog("Biden", 87, 90)
dog3 = PetDog("Obama", 65, 99)

dog1.play(dog2, dog3)

dog2.do_a_trick()