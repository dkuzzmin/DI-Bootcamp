#1
class Farm:
    def __init__(self, name):
        self.animals = {}
        self.name = name
    def add_animal(self, animal, amount = 1):
        
        if animal in self.animals:
            self.animals[animal] += amount
        else:
            self.animals.update({animal:amount})
    def get_info(self):
        print(f"{self.name}'s farm")
        for n in self.animals:
            print(f"{n}: {self.animals[n]}")
 


macdonald = Farm("McDonald")

macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()


# abcdefghijklmnopqrstuvwxyz`


# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!