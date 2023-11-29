#1
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:


s = input("Write your birthday (DD/MM/YYYY):")
n = (123 - int(s[-2:]))%10
#print(n)


print("       _","_"*int((9-n)/2), "!"*n, "_"*int((9-n)/2),"_", sep ="")
#print("       ___iiiii___")
print("      |:H:a:p:p:y:|")
print("    __|___________|__")
print("   |^^^^^^^^^^^^^^^^^|")
print("   |:B:i:r:t:h:d:a:y:|")
print("   |                 |")
print("   ~~~~~~~~~~~~~~~~~~~")

if (s[-2:]) in ["04","08","12","16","20","24","28","32","36","40","44","48","52","56","60","64","68","72","76","80", "84", "88", "92", "96"]:
    print("       _","_"*int((9-n)/2), "!"*n, "_"*int((9-n)/2),"_", sep ="")
    #print("       ___iiiii___")
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")
