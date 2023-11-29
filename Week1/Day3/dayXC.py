
#1
sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict["class"]["student"]["marks"]["history"])


#2
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}

keys_to_remove = ["name", "salary"]
dict = sample_dict.copy()
for x in sample_dict:
    if x in keys_to_remove:
        del dict[x]

# del sample_dict["name"]
# del sample_dict["salary"]

print(dict)


for i in range(1, 3):
    print(i)
else:
    print('The for loop is over')

    