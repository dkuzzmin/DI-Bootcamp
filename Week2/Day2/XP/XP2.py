class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return print(f"{self.name} is barking")
    def run_speed(self):
        speed = self.weight/self.age * 10
        return speed
    def fight(self, other_dog):
        if self.run_speed() * self.weight >= other_dog.run_speed() * other_dog.weight:
            winner = self.name
        else:
            winner = other_dog.name
        return print(f"Winner is {winner}")


# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

dog1 = Dog("Trump", 77, 120)
dog2 = Dog("Biden", 87, 90)
dog3 = Dog("Obama", 65, 99)

dog1.bark()
print(f"{dog1.name}'s speed is {round(dog1.run_speed(),1)}")
dog1.fight(dog2)
dog2.fight(dog3)
