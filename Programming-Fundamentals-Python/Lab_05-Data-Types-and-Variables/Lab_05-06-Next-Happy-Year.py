# 6. Next Happy Year
# You are saying goodbye to your best friend:
# "See you next happy year". Happy Year is the year
# with only distinct digits, for example, 2018.
# Write a program that receives an integer number
# and finds the next happy year.

# Verzija 1

year = int(input()) # definisemo godinu
year += 1 # uvecamo godinu za 1 jer trazimo prvu sledecu godinu
while len(str(year)) != len(set(str(year))):
# uporedjujemo duzinu stringa "year" sa duzinom unikatnog seta
# koriscenjem unikatnog seta, odstranjujemo duplikate cifara
    year += 1 # uvecavamo godinu za 1 i vracamo se na pocetak while petlje
# kada while petlja naidje na prvu sledecu godinu sa unikatnim ciframa
# stampamo tu godinu
print(year)