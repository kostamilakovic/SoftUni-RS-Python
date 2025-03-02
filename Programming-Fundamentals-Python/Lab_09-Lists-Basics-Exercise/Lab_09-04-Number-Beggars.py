# 4. Number Beggars
# You will receive 2 lines of input. On the first line, you will receive
# a single string of integers, separated by a comma and a space ", ".
# On the second line, you will receive a count of beggars.
# Your job is to print a list with the sum of what each beggar brings home,
# assuming they all take regular turns, from the first to the last number in the list.
# For example, [1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6,
# as the first one takes [1, 3, 5], and the second one collects [2, 4].
# The same list with 3 beggars would produce a better outcome
# for the second beggar: 5, 7, and 3, as they will respectively take [1, 4], [2, 5], and [3].
# Also, note that not all beggars have to take the same amount of "offers",
# meaning that the length of the list is not necessarily a multiple of n.
# The list length could be even shorter - i.e., the last beggars will take nothing (0).

# Verzija 1 - koristeci moduo

linija = input()
beggars = int(input())
lista = list(map(int, linija.split(", ")))
sum = [0] * beggars
brojac = 0
for broj in lista:
    sum[brojac % beggars] += broj
    brojac += 1
print(sum)

# Verzija 2 - kombinacijom for/if

# linija = input()
# beggars = int(input())
# lista = list(map(int, linija.split(", ")))
# sum = [0] * beggars
# brojac = 0
# for broj in lista:
#     sum[brojac] += broj
#     brojac += 1
#     if brojac == beggars:
#         brojac = 0
# print(sum)

# Verzija 3 - kombinacijom while/for/if

# linija = input()
# beggars = int(input())
# lista = list(map(int, linija.split(", ")))
# n = 0
# sum = [0] * beggars
# flag = True
# while flag:
#     for i in range(beggars):
#         if n < len(lista):
#             sum[i] = sum[i] + lista[n]
#             n += 1
#         else:
#             flag = False
#             break
# print(sum)