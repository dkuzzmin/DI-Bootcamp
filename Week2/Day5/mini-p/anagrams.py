#This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker 
# for the anagram-related logic.

from anagram_checker import AnagramChecker

flag = True
while flag:
    print("Menu:")
    print("Press 1 to write the word ")
    print("Press 2 to exit")
    user_in = input("1 or 2? :")
    if user_in == "1":
        sw = AnagramChecker()
        word = input("Enter the word to anagram: ").strip()
        
        # validation checks 
        if len(word.split()) > 1:
            print("Error! Too any words")
            continue
        elif not word.isalpha():
            print("Error! Only letters nust be in the word")
        else:
            pass
        
        #my methods
        if sw.is_valid_word(word):


            print(f"YOUR WORD: {word.upper()}")
            print(f"this is a valid English word.")
            w = sw.get_anagrams(word)
            print(f"Anagrams for your word: {", ".join(w)}.")
        else:
            print("Not valid word")



    else:
        flag = False
print("Game Over")
    