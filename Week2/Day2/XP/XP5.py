#5
from XP4 import Family
class TheIncredibles(Family):
    def __init__(self, last_name, members) -> None:
        self.members = members
        self.last_name = last_name 
        super().__init__(members, last_name)

    def use_power(self, name):
        for x in self.members:
            if x["age"] > 18:
                if x["name"] == name:
                    print("!!!!!!!!!")
                    x_name = x["name"]
                    x_power = x["power"]
                    print(f"Super power of {x_name} is {x_power}")
            else:
                raise Exception("Not over 18")
            
    def incredible_presentation(self):
        super().family_presentation()
        print("**Here is our powerful family:**")

data = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

incredibles_fam = TheIncredibles("Incredibles", data)


incredibles_fam.use_power("Sarah")
incredibles_fam.use_power("Michael")

incredibles_fam.family_presentation()

incredibles_fam.born(name='Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='Baby Jack')

incredibles_fam.family_presentation()
