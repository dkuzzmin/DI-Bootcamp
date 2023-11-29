#1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
s = dict(zip(keys, values))
print(s)


#2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
fam_list = []
fam_list.append(family)
print(fam_list)

user = ""
family1 = dict()
while user != "quit":
    user = input("Write name: ")
    u_age = int(input("Write age: "))
    family1[user]= u_age
del family1["quit"]
fam_list.append(family1)
print(fam_list) 

for fam in fam_list:
    sum = 0
    for x in fam.values():
        if x > 12:
            sum+=15
        elif 3 < x <= 12:
            sum+=10
    print("Total ticket sum for family:", fam.keys(),": ", sum)


#3

brand = {"name": "Zara", 
"creation_date": 1975, 
"creator_name": "Amancio Ortega Gaona", 
"type_of_clothes": ["men", "women", "children", "home"], 
"international_competitors": ["Gap", "H&M", "Benetton"], 
"number_stores": 7000, 
"major_color":{ 
    "France": "blue", 
    "Spain": "red", 
    "US": ["pink", "green"]}
}

#  Change the number of stores to 2.
brand["number_stores"] = 2

#  Print a sentence that explains who Zaras clients are.
t = ", ".join(brand["type_of_clothes"])
print (f"Clients of Zara are {t}")

#  Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"

# Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")


# Delete the information about the date of creation.
del brand["creation_date"]

# Print the last international competitor.
print(brand["international_competitors"][-1])

# Print the major clothes colors in the US.
print(brand["major_color"]["US"])

# Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand.keys()))

# Print the keys of the dictionary.
print(brand.keys())

# Create another dictionary called more_on_zara with the following details:
more_zara = {"creation_date": 1975,
              "number_stores": 10000
}

#Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_zara)

#Print the value of the key number_stores. What just happened ?
print(brand)
print("Recovered")



#4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

#>>> print(disney_users_A)
#{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
disney_users_A = dict()
for i in users:
    disney_users_A[i] = users.index(i)
print(disney_users_A)


# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
disney_users_B = dict()
for i in users:
    disney_users_B[users.index(i)] = i
print(disney_users_B)

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

disney_users_C = dict()
users.sort()
for i in users:
    disney_users_C[i] = users.index(i)
print(disney_users_C)


# The characters, which names contain the letter “i”.
disney_users_A = dict()
for i in users:
    if "i" in i:
        disney_users_A[i] = users.index(i)
print(disney_users_A)


# The characters, which names start with the letter “m” or “p”.
disney_users_A = dict()
for i in users:
    if "m" == i[0].lower() or "p" == i[0].lower():
        disney_users_A[i] = users.index(i)
print(disney_users_A)




