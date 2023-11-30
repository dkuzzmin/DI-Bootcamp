#1
s_input = "without,hello,bag,world"
# bag,hello,without,world

# s_output = s_input.split(",")
# s_output.sort()
# print(', '.join(s_output))

print (', '.join([num for num in sorted(s_input.split(","))]))



