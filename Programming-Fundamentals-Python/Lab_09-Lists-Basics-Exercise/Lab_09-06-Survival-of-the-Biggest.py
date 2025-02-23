# 6. Survival of the Biggest
# Write a program that receives a list of integer numbers
# (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list.
# You should remove the smallest ones, and then, you should print
# all the numbers that are left in the list, separated by a comma and a space ", ".

# Verzija 1

# linija = input()
# n = int(input())
# lista = list(map(int, linija.split()))
# sortirana = sorted(lista)
# for i in range(n):
#     lista.remove(sortirana[i])
# print(", ".join(map(str, lista)))

# Verzija 2 - pomocu min() integrisane funkcije

linija = input()
n = int(input())
lista = list(map(int, linija.split()))
for i in range(n):
    lista.remove(min(lista))
print(", ".join(map(str, lista)))