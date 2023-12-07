#1 Exercise 1 – Random Sentence Generator


import os
from random import randint

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_words_from_file():
    with open(dir_path + "//sowpods.txt", 'r') as f:
        text = f.readlines()
    
    cleaned_text = list(map(lambda s: s.strip('\n'), text))
    # print(text[:50])
    # print(cleaned_text[:50])
    return cleaned_text

def get_random_sentence(length):
    w = []
    for i in range(length):
        w.append(get_words_from_file()[randint(1,len(get_words_from_file()))])
    return " ".join(w)

def main():
    print("""Program will get you sentence how long that you want. Sentence will be make from randomly from word dictionary
          
          """) 
    len_user = int(input("How many words do you want?(from 2 to 20):"))
    if 2 <= len_user <= 20:
        print(f"Your sentence: {get_random_sentence(len_user).lower()}")
    else:
        print(f"Wrong quantity")


print(type(get_words_from_file()))
#print(get_words_from_file()[:50])
print(get_random_sentence(5).lower())

main()




