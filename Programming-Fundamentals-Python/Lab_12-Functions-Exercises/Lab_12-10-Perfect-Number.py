# 10. Perfect Number
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# •	"We have a perfect number!" - if the number is perfect.
# •	"It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.

def perfect_number (number):
    if number < 1:
        return "It's not so perfect."
    divisor_sum = sum([n for n in range (1, number) if number % n == 0])
    if divisor_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."
print(perfect_number(int(input())))