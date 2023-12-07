
import string


import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class Text():
    def __init__(self, stringtext) -> None:
        self.stringtext = stringtext
    def frequency(self, word):
        word_counts = self.stringtext.lower().split().count(word)
        if word_counts > 0:
            return word_counts
        else:
            return None
    def mostcommon(self):
        max = 0
        max_word = ""
        for x in self.stringtext.lower().split():
            if self.frequency(x) > max:
                max = self.frequency(x)
                max_word = x
        return max_word

    def uniquewords(self):
        return list(set(self.stringtext.lower().split()))

    @classmethod
    def from_file(cls, textfile):
        with open(textfile, "r") as f:
            x = f.read()
            return cls(x)



txt = Text("Today, is a happy happy day happy day")
print(f"Frequency is {txt.frequency("day")}")

print(f"Most common word is '{txt.mostcommon()}'")

print(txt.uniquewords())

txt1 = txt.from_file(dir_path + "/the_stranger.txt")

print(txt1.frequency("and"))
print(txt1.frequency("albert"))
# print(txt1.mostcommon())
# print(txt1.uniquewords())



class TextModification(Text):
    def filterdatapunk(self):
        f_data = []
        for w in self.stringtext.split():
            w1=""
            for s in range(0,len(w)):
                if w[s] not in string.punctuation:
                    w1+=w[s]
            w = w1
            f_data.append(w)
        return " ".join(f_data)

    def filterdatastop(self):
        STOP_WORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 
'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
        f_data = []
        for w in self.stringtext.lower().split():
            if w not in STOP_WORDS:
                f_data.append(w)
        return " ".join(f_data)




txt = TextModification("Today, is a happy happy day happy day")
print(txt.filterdatastop())

print(txt.filterdatapunk())


# print(string.punctuation)