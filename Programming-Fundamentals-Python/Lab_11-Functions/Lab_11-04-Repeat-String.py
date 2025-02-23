# 4. Repeat String
# Write a function that receives a string and a counter n.
# The function should return a new string – the result of repeating the old string n times.
# Print the result of the function. Try using lambda.

# Verzija 1

# def n_string (linija, n):
#     return linija * n
#
# linija = input()
# n = int(input())
# print(n_string(linija, n))

# Verzija 2 - koristeci lambda

linija = input()
n = int(input())
n_string = lambda a, b: a * b
print(n_string(linija, n))

# LAMBDA je najsmisleniji kada se koristi uz funkciju map()