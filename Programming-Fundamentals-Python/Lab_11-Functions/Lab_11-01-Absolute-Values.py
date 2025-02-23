# 1. Absolute Values
# Write a program that receives a sequence of numbers, separated by a single space,
# and prints their absolute value as a list. Use abs().

# Verzija 1 - pomocu funkcije

# def abs_lista (lista):
#     return list(abs(element) for element in lista)
#
# linija = input()
# lista = list(map(float, linija.split(" ")))
# print(abs_lista(lista))

# Verzija 2 - koristeci lambda

# linija = input()
# lista = list(map(float, linija.split(" ")))
# abs_lista = list(map(lambda x: abs(x), lista))
# print(abs_lista)

linija = input()
abs_lista = list(map(lambda x: abs(float(x)), linija.split(" ")))
print(abs_lista)