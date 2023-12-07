import os

dir_path = os.path.dirname(os.path.realpath(__file__))



with open('/Users/skyhome/Desktop/DI-Bootcamp/Week2/Day4/example.txt', encoding="utf-8", mode="r+") as f:
    my_line = "Hello"
    print("jhhhh")
    # f.write() +=my_line
    original_text = f.read()
    my_line = original_text + "Hiiiii"
    f.write(my_line)

def read_file(file_name):
    with open(file_name, encoding="utf-8", mode="r") as f:
        file_text = f.readlines()
        return file_text

def read_and_write(file_name, text_add):
    with open(file_name, encoding="utf-8", mode="r+") as f:
        f.read()
        f.write(f"\n{text_add}")
        final_f = f.read()
        return final_f
# read_and_write("/Users/skyhome/Desktop/DI-Bootcamp/Week2/Day4/example.txt'", 'addind from function')
# print(read_and_write("/Users/skyhome/Desktop/DI-Bootcamp/Week2/Day4/example.txt'", 'addind from function'))
# print(read_file("/Users/skyhome/Desktop/DI-Bootcamp/Week2/Day4/example.txt"))



# Read the file line by line
with open("/Users/skyhome/Desktop/DI-Bootcamp/Week2/Day4/starwars.txt", 'r') as f:
    text = f.readlines()
    print(text)
# Read only the 5th line of the file
# for line in text[10]:
#     print(line)

# for i,line in enumerate(text, start = 1):
#     if line == 5:    
#         print(line)

print(text[4])




# Read only the 5 first characters of the file
print(text[:5])
# Read all the file and return it as a list of strings. Then split each word
# splited = [w.split() for w in text]

for word in text:
    s = list(word)
    print(s)
# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file

cleaned_names = list(map(lambda s: s.strip('\n'), text))
darth = cleaned_names.count("Darth")
lea = cleaned_names.count("Lea")
luke = cleaned_names.count("Luke")
print(darth, lea, luke)


# Append your first name at the end of the file
with open(dir_path + "\\starwars.txt", mode = "a") as f:
    print()

# Append "SkyWalker" next to each first name "Luke"

