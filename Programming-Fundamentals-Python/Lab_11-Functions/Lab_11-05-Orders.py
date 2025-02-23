# 5. Orders
# Write a function that calculates the total price of an order and returns it.
# The function should receive one of the following products:
# "coffee", "coke", "water", or "snacks", and a quantity of the product.
# The prices for a single piece of each product are:
# coffee - 1.50
# water - 1.00
# coke - 1.40
# snacks - 2.00
#
# Print the result formatted to the second decimal place.

def orders (product, quantity):
    if product == "coffee":
        price = 1.50 * quantity
    elif product == "water":
        price = 1.00 * quantity
    elif product == "coke":
        price = 1.40 * quantity
    elif product == "snacks":
        price = 2.00 * quantity
    return price
product=input()
quantity=int(input())
print(f"{orders(product,quantity):.2f}")