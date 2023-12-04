#1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def findcat(cats):
    max = 0
    maxname = ""
    for x in cats:
        if x.age > max:
           max = x.age 
           maxname = x.name
    return print(f"The oldest cat is {maxname}, and is {max} years old.")   

firstcat = Cat("Marusya", 5)
secondcat = Cat("Masha", 3)
thirdcat = Cat("Masya", 15)
findcat([firstcat,secondcat,thirdcat])

#2

class Dog:
    def __init__(self, name, height) -> None:
        self.name = name
        self.height = height
    def bark(self):
        print (f"{self.name} goes woof!")
        return
    def jump(self):
        print (f"{self.name} jumps {self.height} cm high!”. {self.height} is the height"*2)
        return
dog1 = Dog("Muhtar", 55)
dog1.bark()
dog1.jump()

davids_dog = Dog("Rex", 50)
print(davids_dog.name, davids_dog.height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger")
else:
    print(f"{sarahs_dog.name} is bigger")


#3
class Song:
    def __init__(self, lyrics:list):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for x in self.lyrics:
            print(x)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#4
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name 
    def add_animal(self, new_animal):
        self.animals.append(new_animal)
        return self.animals
    def get_animals(self):
        return print(self.animals)
    def sell_animal(self, animal_sold):
        self.animals.remove(animal_sold)
        return self.animals
    def sort_animals(self):
        self.animals.sort()
        an = {}
        char = ""
        group = 0       
        for x in self.animals: 
            # print(x,"lett ",x[0], char, "key ", group)
            char1 = x[0]
            if char1 != char:
                group += 1
                char = char1
                an[group] = [x]
            else:
                an[group].append(x)
            # print("current: ", an)
        return an
    def get_groups(self, animals:dict):
        for x,y in animals.items():
            print (f"Group {x} animals: {', '.join(y)}")
        
        


ramat_gan_safari = Zoo("Ramat Gan")
ramat_gan_safari.animals = ['Cat', "Ape", 'Eel', "Baboon", "Bear", 'Cougar','Emu']

ramat_gan_safari.get_animals()
ramat_gan_safari.add_animal("Tiger")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Ape")
ramat_gan_safari.get_animals()
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups(ramat_gan_safari.sort_animals())


















