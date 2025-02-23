# 7. Rounding
# Write a program that rounds all the given numbers, separated by a single space,
# and prints the result as a list. Use round().

# linija = input()
# lista = list(map(lambda x: round(x), linija.split(" ")))
# print(lista)

# Verzija 2 - koristeci funkciju

def rounding(lista):
    return list(map(abs, lista))
lista = list(map(float, input().split()))
print(rounding(lista))