# 3. Elevator
# Calculate how many courses will be needed
# to elevate N persons by using an elevator
# with a capacity of P persons.
# The input holds two lines: the number of people N
# and the capacity P of the elevator.

# Verzija 1 - if
# ovo je brza verzija jer nece iterirati kroz svaku voznju
# vec prostim celobrojnim deljenjem vidimo koliko puta ce se
# lift popuniti i onda proverimo da li je ostatak razlicit od nule,
# ako je neko ostao, dodajemo jos jednu voznju.

people = int(input())
capacity = int(input())
courses = people // capacity
if people % capacity != 0:
    courses += 1
print(courses)

# Verzija 2 - while petlja

# people = int(input())
# capacity = int(input())
# courses = 0
# while people > 0:
#     people -= capacity
#     courses += 1
# print(courses)