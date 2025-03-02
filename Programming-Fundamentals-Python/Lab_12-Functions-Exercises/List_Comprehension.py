# List comprehension is a way to create lists using a concise syntax. It allows us to generate
# a new list by applying an expression to each item in an existing iterable (such as a list or range).
# This helps us to write cleaner, more readable code compared to traditional looping techniques.
# For example, if we have a list of integers and want to create a new list containing the square of
# each element, we can easily achieve this using list comprehension.

a = [2,3,4,5]
res = [val ** 2 for val in a]
print(res)

# Syntax of list comprehension
# [expression for item in iterable if condition]
# expression: # The transformation or value to be included in the new list.
# item: # The current element taken from the iterable.
# iterable: # A sequence or collection (e.g., list, tuple, set).
# if condition (optional): # A filtering condition that decides whether the current item should be included.

# Conditional statements in list comprehension
a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res) # [2, 4]

# Creating a list from a range
a = [i for i in range(10)]
print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using nested loops
# Creates a list of tuples representing all combinations of (x, y)
# where both x and y range from 0 to 2.
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(coordinates) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# Flattening a list of lists
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)