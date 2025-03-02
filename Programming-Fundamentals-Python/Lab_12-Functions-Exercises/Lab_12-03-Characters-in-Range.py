# 3. Characters in Range
# Write a function that receives two characters and returns a single string
# with all the characters in between them (according to the ASCII code),
# separated by a single space. Print the result on the console.

# Verzija 1: koristeći listu

def characters_in_range(a, b):
    list = []
    for char in range(ord(a)+1, ord(b)):
        list.append(chr(char))
    print(" ".join(list))
characters_in_range(input(), input())

# Verzija 2: koristeci print end=" "

# def characters_in_range(a, b):
#     for char in range(ord(a)+1, ord(b)):
#         print(chr(char), end=" ")
# characters_in_range(input(), input())