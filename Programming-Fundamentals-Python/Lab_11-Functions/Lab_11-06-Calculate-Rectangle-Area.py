# 6. Calculate Rectangle Area
# Create a function that calculates and returns the area of a rectangle
# by a given width and height. Print the result on the console.

# Verzija 1 - koristeci lambda

a = int(input())
b = int(input())
pravougaonik = lambda a,b: a*b
print(pravougaonik(a,b))

# Verzija 2 - koristeci funkciju

def pravougaonik(a,b):
    return a*b
a = int(input())
b = int(input())
print(pravougaonik(a,b))