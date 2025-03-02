# 8. Palindrome Integers
# A palindrome is a number that reads the same backward as forward,
# such as 323 or 1001. Write a function that receives a list of positive integers,
# separated by comma and space ", ". The function should check if each integer
# is a palindrome - True or False. Print the result.

# lista [::-1] pravi listu od [ end : 0 : -1 ]
# tj. obrce redosled jer -1 znaci da je pocetak zapravo kraj liste
# lista [::1]

# Verzija 1

def is_palindrome (number):
    s = number
    return s == s[::-1]

def palindrom_integers (input_numbers):
    list_numbers = input_numbers.split(", ")
    for number in list_numbers:
        print(is_palindrome(number))

palindrom_integers(input())

# Verzija 2: koristeci List Comprehension
# 1. napravimo funkciju koja jedan broj proverava da li je palindrom
# 2. koristeci List Comprehension pravimo niz boolean vrednosti
# za svaki clan liste provucen kroz funkciju provere palindroma
# 3. koristeci for petlju stampamo svaki element niza odvojeno

# def is_palindrome (mapa):
#     lista = [c for c in str(mapa)]
#     leva = "".join(lista)
#     desna = "".join(lista[::-1])
#     if leva == desna:
#         return True
#     else:
#         return False
#
# resenje = list(map(is_palindrome, map(int, input().split(","))))
# for r in resenje:
#     if r == True:
#         print(True)
#     else:
#         print(False)