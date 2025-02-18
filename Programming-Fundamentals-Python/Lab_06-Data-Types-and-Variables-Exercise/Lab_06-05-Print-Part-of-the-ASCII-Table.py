# 5. Print Part of the ASCII Table
# Write a program that prints part of the ASCII table characters
# on the console, separated by a single space. On the first
# line of input, you will receive the char index you should
# start with. On the second line - the index of the last
# character you should print.

index1 = int(input())
index2 = int(input())
for i in range(index1, index2+1):
    print(chr(i), end=" ")