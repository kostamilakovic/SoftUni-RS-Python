# 6. Sort
# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order. Use sorted().

# Verzija 1: koristeci metod .sort()
# sortira listu in-place pa je vraca sortiranu

# def sorter_list (sequence_of_numbers):
#     list_of_numbers = list(map(int, sequence_of_numbers.split()))
#     list_of_numbers.sort()
#     return list_of_numbers
# print(sorter_list(input()))

# Verzija 2: koristeci ugradjenu funkciju sorted()
# sortira listu tokom pozivanja unutar print()

def sorter_list (sequence_of_numbers):
    list_of_numbers = list(map(int, sequence_of_numbers.split()))
    return list_of_numbers
print(sorted(sorter_list(input())))