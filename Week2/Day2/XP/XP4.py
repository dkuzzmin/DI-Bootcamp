#4
class Family():
    def __init__(self, members, last_name) -> None:
        self.members = members
        self.last_name = last_name
    def born(self, **kwargs):
        self.members.append(kwargs)
        print("Congrats with newborn!")

    def is_18(self, name):
        for x in self.members:
            if x["name"] == name:
                return x["age"] >= 18
        return False     

    def family_presentation(self):
        print(f"The {self.last_name}'s Family:")
        for x in self.members:
            print("- ", x["name"]," (",x["age"],"years old), gender is", x["gender"])

f = [
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':3,'gender':'Female','is_child':False}
    ]

f1 = Family(f, "Akselrod")

f1.born(name = "Bobby", age = 15, gender = "Male", is_child = True)
print(f1.is_18("Michael"))
print(f1.is_18("Sarah"))
# print(f1.members)

f1.family_presentation()
