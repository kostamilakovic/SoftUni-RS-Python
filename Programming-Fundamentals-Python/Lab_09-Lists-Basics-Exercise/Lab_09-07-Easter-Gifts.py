# 7. * Easter Gifts
# Create a program that helps you plan the gifts for your friends and family.
# First, you are going to receive the gifts you plan on buying on a single line,
# separated by space, in the following format:
# "{gift1} {gift2} {gift3}... {giftn}"
# Then you will start receiving commands until you read the "No Money" message.
# There are three possible commands:
# "OutOfStock {gift}"
# Find the gifts with this name in your collection, if any, and change their values to "None".
# "Required {gift} {index}"
# If the index is valid, replace the gift on the given index with the given gift.
# "JustInCase {gift}"
# Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with the value "None",
# separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
# On the 1st line,  you will receive the names of the gifts, separated by a single space.
# On the following lines, until the "No Money" command is received,
# you will be receiving commands.
# The input will always be valid.
# Output
# Print the gifts in the format described above.

lista = input().split()
komanda = input()

while komanda != "No Money":
    delovi_komande = komanda.split()
    if delovi_komande[0] == "OutOfStock":
        for i, element in enumerate(lista):
            if element == delovi_komande[1]:
                lista[i] = "None"
    elif delovi_komande[0] == "Required":
        index = int(delovi_komande[2])
        if 0 <= index < len(lista):
            lista[index] = delovi_komande[1]
    elif delovi_komande[0] == "JustInCase":
        lista[-1] = delovi_komande[1]
    komanda = input()
while "None" in lista:
    lista.remove("None")
print(" ".join(map(str, lista)))