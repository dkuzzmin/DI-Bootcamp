import json

my_family = {
    "parents":['Beth', 'Jerry'],
    "children":['Summer', 'Morty']
}

json_file = "family.json"

with open(json_file, 'w') as file_obj:
    json.dump(my_family, file_obj)
   #json.dump(obj2save , destination_file)






import json

json_file = 'family.json'
with open(json_file, 'r') as file_obj:
    my_family = json.load(file_obj)

print(my_family)
#>> {'children': ['Summer', 'Morty'], 'parents': ['Beth', 'Jerry']} 


