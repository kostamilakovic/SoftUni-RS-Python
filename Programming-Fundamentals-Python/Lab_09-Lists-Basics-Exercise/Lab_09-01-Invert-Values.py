# 1. Invert Values
# Write a program that receives a single string containing
# positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.

# Verzija 1 - koristeci map() funkciju

word = input()
lista = list(map(int, word.split(" ")))
nova_lista = []
for broj in lista:
    nova_lista.append(broj * -1)
print(nova_lista)

# Verzija 2 - izmenom clanova liste

# word = input()
# lista = list(map(int, word.split(" ")))
# for i in range(0, len(lista)):
#     lista[i] = lista[i] * -1
# print(lista)