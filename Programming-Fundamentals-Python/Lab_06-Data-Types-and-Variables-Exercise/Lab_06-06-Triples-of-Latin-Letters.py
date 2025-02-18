# 6. Triples of Latin Letters
# Write a program to read an integer N and print all triples
# of the first N small Latin letters, ordered alphabetically.
# Example: Input = 3, Output = aaa, aab, aac ... ccc

# Verzija 1 - koristeci 97 (vrednost karaktera 'a') unutar range()

n = int(input())
for i in range(97, 97 + n):
    for j in range(97, 97 + n):
        for k in range(97, 97 + n):
            print(chr(i)+chr(j)+chr(k))

# Verzija 2 - koristeci ord('a') unutar range()

# n = int(input())
# for i in range(ord('a'), ord('a') + n):
#     for j in range(ord('a'), ord('a') + n):
#         for k in range(ord('a'), ord('a') + n):
#             print(chr(i)+chr(j)+chr(k))

# TIPS:
# ASCII kodovi za mala slova alfabeta su od 97 do 122.