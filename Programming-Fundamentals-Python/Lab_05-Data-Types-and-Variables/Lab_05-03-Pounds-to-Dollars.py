# 3. Pounds to Dollars
# Write a program that converts British pounds (integer)
# to US dollars formatted to the 3rd decimal point.
# 1 British Pound = 1.31 Dollars.

# Verzija 1

pounds = int(input())
print(f"{(pounds*1.31):.3f}") # konvertujemo funte u dolare direktno u print()

# Verzija 2

pounds = int(input())
dollars = pounds*1.31 # prvo konvertujemo funte u dolare
print(f"{dollars:.3f}") # zatim ispisujemo dolare koristeci print()