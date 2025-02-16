# 4. Centuries to Minutes
# Write a program that reads an integer number of centuries
# and converts it to years, days, hours, and minutes.
# Assume that one year has 365.2422 days on average (the Tropical year).

# Verzija 1

centuries = int(input()) # unosimo broj vekova
years = centuries * 100 # racunamo godine, svaki vek ima 100 godina
days = int(years * 365.2422) # racunamo dane i pretvaramo ih u integer da bi odstranili decimalni deo
hours = days * 24 # racunamo sate, svaki dan ima 24 sata
minutes = hours * 60 # racunamo minute, svaki sat ima 60 minuta
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")