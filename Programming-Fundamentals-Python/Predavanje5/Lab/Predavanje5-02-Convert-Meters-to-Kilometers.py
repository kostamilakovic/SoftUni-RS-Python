# 2. Convert Meters to Kilometers
# You will be given an integer that represents a distance in meters.
# Write a program that converts meters to kilometers
# formatted to the second decimal point.

# Verzija 1
meters = int(input())
print(f"{(meters/1000):.2f}") # metre pretvaramo u km direktno u print()

# Verzija 2
# meters = int(input())
# km = meters/1000 # km deklarisemo pre print()
# print(f"{km:.2f}") # a zatim pozovemo km iz print()
