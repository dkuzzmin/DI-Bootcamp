#1
s_input = "without,hello,bag,world"
# bag,hello,without,world

# s_output = s_input.split(",")
# s_output.sort()
# print(', '.join(s_output))

print (', '.join([num for num in sorted(s_input.split(","))]))



#2
# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
# Examples
# longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"

def longestword(s_in): 
    s = s_in.split(" ")
    s1 = [s1.replace(".","") for s1 in s]
    return max(s1, key = len)

print(longestword("Margaret's toy is a pretty doll."))




