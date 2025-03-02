# 12. Factorial Division
# Write a function that receives two integer numbers.
# Calculate the factorial of each number.
# Divide the first result by the second
# and print the division formatted to the second decimal point.

from math import factorial

def factorial_division (a, b):
    factorial1 = factorial(a)
    factorial2 = factorial(b)
    result = factorial1 / factorial2
    return f"{result:.2f}"
print(factorial_division(int(input()), int(input())))