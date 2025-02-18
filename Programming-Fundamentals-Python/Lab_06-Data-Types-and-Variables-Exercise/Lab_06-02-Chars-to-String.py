# 2. Chars to String
# Write a function that receives 3 characters.
# Concatenate all the characters into one string
# and print it on the console.

# Verzija 1 - podrazumevani unos po jednog karaktera

char1 = input()
char2 = input()
char3 = input()
concatenated = char1+char2+char3
print(concatenated)

# Verzija 2 - unos po jednog karaktera
# ukoliko bi zeleli da sabiramo samo stringove od jednog karaktera
# prvo bi proverili da li je svaki unos bio jedan karakter
# posto python nema tip podatka koji je jedan karakter
# kao sto recimo C++ ima "char" tip

# char1 = input()
# char2 = input()
# char3 = input()
# if len(char1) == 1 and len(char2) == 1 and len(char3) == 1:
#     concatenated = char1 + char2 + char3
#     print(concatenated)
# else:
#     pass

# TIPS
# Stringove osim sabiranja mozemo i da množimo.