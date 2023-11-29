#1
m = [
["7", "i", "i"],
["T", "s", "x"],
["h", "%", "?"],
["i", " ", "#"],
["s", "M", " "],
["$", "a", " "],
["#", "t", "%"],
["^", "r", "!"]
]

w = " " #secret word
# for i in range(len(m)):
#     for j in range(len(m[i])):
#         if (m[i][j]).isalpha():
#             w = w + m[i][j]
# print(w)
for i in range(len(m[0])):
    for j in range(len(m)):
        if (m[j][i]).isalpha():
            w = w + m[j][i]
        else:
            if w[-1] != " ":
                w = w + " "
w = w[1:]

print(w)






