# 4. Search
# On the first line, you will receive a number n.
# On the second line, you will receive a word.
# On the following n lines, you will be given some strings.
# You should add them to a list and print them.
# After that, you should filter out only the strings
# that include the given word and print that list too.

# Verzija 1 - pravimo istovremeno obe liste

n = int(input())
rech = input()
lista = []
filtrirana_lista = []
for i in range(n):
    nova_rech = input()
    lista.append(nova_rech)
    if rech in nova_rech:
        filtrirana_lista.append(nova_rech)
print(lista)
print(filtrirana_lista)

# Verzija 2 - pravimo prvu listu pa je filtriramo

# n = int(input())
# rech = input()
# lista = []
# for i in range(n):
#     nova_rech = input()
#     lista.append(nova_rech)
# print(lista)
# for i in range(len(lista)-1,-1,-1):
#     nova_rech=lista[i]
#     if rech not in nova_rech:
#         lista.remove(nova_rech)
# print(lista)

# Verzija 3 - pravimo prvu listu pa drugu na osnovu filtriranja prve

# n = int(input())
# rech = input()
# lista = []
# filtrirana_lista = []
# for i in range(n):
#     nova_rech = input()
#     lista.append(nova_rech)
# for i in range(0,len(lista)):
#     nova_rech=lista[i]
#     if rech in nova_rech:
#         filtrirana_lista.append(nova_rech)
# print(lista)
# print(filtrirana_lista)