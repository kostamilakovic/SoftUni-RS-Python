# 4. Odd and Even Sum
# You will receive a single number.
# You should write a function that returns the sum
# of all even and all odd digits in a given number.
# The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.

# Verzija 1

def odd_even_sum (n):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for i in range(len(str(n))):
        broj = n % 10
        if broj % 2 == 0:
            sum_of_even_digits += broj
        else:
            sum_of_odd_digits += broj
        n = n // 10
    print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
odd_even_sum(int(input()))