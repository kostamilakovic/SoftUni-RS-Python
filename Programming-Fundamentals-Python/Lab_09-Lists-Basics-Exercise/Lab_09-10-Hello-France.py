# 9. * Hello, France
# You want to go to France by train, and the train ticket costs exactly 150$.
# You do not have enough money, so you decide to buy some items within your budget
# and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type	Maximum Price
# Clothes	50.00
# Shoes	35.00
# Accessories	20.50
# If the price for a particular item is higher than the maximum price, don't buy it.
# Every time you buy an item, you have to reduce the budget with its price value.
# If you don't have enough money for it, you can't buy it. Buy as many items as you can.
# Next, you should increase the price of each item you have successfully bought by 40%
# and then sell it. Calculate if the budget after selling all the items is enough
# to buy the train ticket.
# Input / Constraints
# On the 1st line, you will receive the items with their prices
# in the format described above – real numbers in the range [0.00……1000.00]
# On the 2nd line, you are going to be given the budget
# a real number in the range [0.0….1000.0]
# Output
# First, print the list with the bought item’s new prices, formatted to the second decimal point in the following format:
# "{price1} {price2} {price3} … {priceN}"
# Second, print the profit, formatted to the second decimal point in the following format:
# "Profit: {profit}"
# •	Finally:
# If the budget is enough to buy the train ticket, print: "Hello, France!"
# Otherwise, print: "Not enough money."

# Verzija 1: koristeci petlje i vise nizova

linija = input()
spisak = linija.split("|")
budzet = float(input())
pocetni_budzet = budzet
max_cena = { "Clothes" : 50.00, "Shoes" : 35.00, "Accessories" : 20.50 }
kupljene_stvari = []
for element in spisak:
    artikal, cena = element.split("->")
    cena = float(cena)
    if cena <= max_cena[artikal] and budzet >= cena:
        kupljene_stvari.append(cena)
        budzet -= cena
prodajne_cene = [trosak * 1.4 for trosak in kupljene_stvari]
profit = sum(prodajne_cene) - sum(kupljene_stvari)
finalni_budzet = pocetni_budzet + profit
# finalni_budzet = budzet + sum(prodajne)
print(" ".join(f"{price:.2f}" for price in prodajne_cene))
print(f"Profit: {profit:.2f}")
if finalni_budzet >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

#Verzija 2: koristeci petlje i manje nizova

# linija = input()
# spisak = linija.split("|")
# budzet = float(input())
# ostatak = budzet
# profit = 0.0
# for element in spisak:
#     razdvojen_spisak = element.split("->")
#     roba = razdvojen_spisak[0]
#     cena = float(razdvojen_spisak[1])
#     if roba == "Clothes" and cena <= 50.00 and ostatak-cena >= 0:
#         ostatak -= cena
#         profit += cena*1.4-cena
#         print(f"{(cena * 1.4):.2f}", end=" ")
#     elif roba == "Shoes" and cena <= 35.00 and ostatak-cena >= 0:
#         ostatak -= cena
#         profit += cena*1.4-cena
#         print(f"{(cena * 1.4):.2f}", end=" ")
#     elif roba == "Accessories" and cena <= 20.50 and ostatak-cena >= 0:
#         ostatak -= cena
#         profit += cena*1.4-cena
#         print(f"{(cena * 1.4):.2f}", end=" ")
# print(f"\nProfit: {profit:.2f}")
# if profit + budzet >= 150:
#     print("Hello, France!")
# else:
#     print("Not enough money.")