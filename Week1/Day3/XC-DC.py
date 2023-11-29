#1
word = input("Write a word: ").lower()
#word = "froggy"
word_dict = dict()


for i in range(len(word)):
    if word[i] in word_dict.keys():
        word_dict[word[i]].append(i)
    else:
        word_dict[word[i]] = [i]
print(word_dict)


2#

items_purchase = {
  "Water": "$2",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}


wallet = "$100"

wallet1 = wallet
for i in range(len(wallet)):
    if wallet[i] not in "0123456789":
        wallet1 = wallet[:i]+wallet[i+1:]
wallet1 = int(wallet1)

mylist = list()
sum = "0"
for key, value in items_purchase.items():
    #transform value to integer
    value1 = ""
    for i in value:
        if i in "0123456789":
             value1 = value1 + i
    value1 = int(value1)

    #making a result list
    if value1 <= wallet1:
        mylist.append(key)
mylist.sort()
if mylist == []:
    print("Nothing")
else:
    print(mylist)




