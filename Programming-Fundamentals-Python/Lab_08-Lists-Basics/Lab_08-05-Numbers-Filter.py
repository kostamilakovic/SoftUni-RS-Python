# 5. Numbers Filter
# On the first line, you will receive a single number n.
# On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# even
# odd
# negative
# positive
# Filter all the numbers that fit in the category
# (0 counts as a positive and even).
# Finally, print the result.

# Verzija 1 - pomocu jedne IF grane

n = int(input())
lista = []
filtrirana_lista = []
for i in range(n):
    broj = int(input())
    lista.append(broj)
komanda = input()
for broj in lista:
    if ((komanda == "even" and broj % 2 == 0) or (komanda == "odd" and broj % 2 != 0) or
            (komanda == "negative" and broj < 0) or (komanda == "positive" and broj >= 0)):
        filtrirana_lista.append(broj)
print(filtrirana_lista)

# Verzija 2 - pomocu vise IF grana

# n = int(input())
# lista = []
# filtrirana_lista = []
# for i in range(n):
#     broj = int(input())
#     lista.append(broj)
# komanda = input()
# if komanda == "even":
#     for i in range(0, len(lista)):
#         privremeni_broj = lista[i]
#         if privremeni_broj % 2 == 0:
#             filtrirana_lista.append(privremeni_broj)
# elif komanda == "odd":
#     for i in range(0, len(lista)):
#         privremeni_broj = lista[i]
#         if privremeni_broj % 2 != 0:
#             filtrirana_lista.append(privremeni_broj)
# elif komanda == "negative":
#     for i in range(0, len(lista)):
#         privremeni_broj = lista[i]
#         if privremeni_broj < 0:
#             filtrirana_lista.append(privremeni_broj)
# elif komanda == "positive":
#     for i in range(0, len(lista)):
#         privremeni_broj = lista[i]
#         if privremeni_broj >= 0:
#             filtrirana_lista.append(privremeni_broj)
# print(filtrirana_lista)