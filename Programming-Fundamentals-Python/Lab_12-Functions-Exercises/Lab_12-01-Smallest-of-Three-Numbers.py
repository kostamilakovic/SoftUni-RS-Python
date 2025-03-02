# 1. Smallest of Three Numbers
# Write a function that receives three integer numbers and returns the smallest.
# Print the result on the console. Use an appropriate name for the function.

# Verzija 1: pomocu min() integrisane funkcije koja radi sa listama

def smallest_of_three (a, b, c):
    lista = [a, b, c]
    return min(lista)

a = int(input())
b = int(input())
c = int(input())
print(smallest_of_three(a,b,c))