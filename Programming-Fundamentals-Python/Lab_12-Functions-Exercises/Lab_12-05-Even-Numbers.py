# 5. Even Numbers
# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().
from enum import nonmember


# Verzija 1: koristeci list comprehension

# def parni_brojevi (string):
#     return [broj for broj in list(map(int, string.split())) if broj % 2 == 0]
# print(parni_brojevi(input()))

# Verzija 2: koristeci ugnjezdene funkcije i filter()
# map() ne mora da se pretvara u listu ako necemo da je direktno stampamo

# def parni_brojevi (string):
#     lista = map(int, string.split())
#     def parni (n):
#         return n % 2 == 0
#     return list(filter(parni, lista))
# print(parni_brojevi(input()))

# Verzija 3: isto kao verzija 2 samo sto je logika funkcije parni()
# vidljivo razdvojena na true i false za dalje koriscenje u filter() funkciji

def parni_brojevi (string):
    def parni (n):
        if n % 2 == 0:
            return True
        else:
            return False
    lista = list(map(int, string.split()))
    lista = list(filter(parni, lista))
    print(lista)
parni_brojevi(input())