#Anagram Checker
import string
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def is_anagram(word1:string, word2:string):
    w1 = list(str(word1.lower()))
    w2 = list(str(word2.lower()))
    w1.sort()
    w2.sort()
    # print(w2)
    # print(w1)
    return (w1 == w2) and (len(w1) == len(w2)) and word1.lower() != word2.lower()

class AnagramChecker:
    def __init__(self):
        with open(dir_path + "//sowpods.txt", 'r') as f:
            self.text = f.readlines()
        cleaned_text = list(map(lambda s: s.strip('\n'), self.text))
        self.text = cleaned_text
        # print( cleaned_text[:20])

    def is_valid_word(self, word):
        if word.upper() in self.text:
            # print("Valid word!")
            return True
        else:
            # print("Not valid word!")
            return False

    def get_anagrams(self, word):
        anagram_list = []
        for w in self.text:
            if is_anagram(w,word):
                anagram_list.append(w)
        return anagram_list

   

    
    # def __str__(self) -> str:
    #     if self.currency == "dollar":
    #         x = f"{str(self.amount)} dollars"
    #     elif  self.currency == "shekel":
    #         x = f"{str(self.amount)} shekels"
    #     return x
    # def __int__(self):
    #     x = int(self.amount)
    #     return x

x1 = AnagramChecker()


if x1.is_valid_word("all"):
    print("Valid word!")
else:
    print("Not valid word!")

print()

print(is_anagram("Meat", "WINN"))
print(is_anagram("Meat", "Team"))
print(x1.get_anagrams("Meat"))