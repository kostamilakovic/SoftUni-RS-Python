# 3. Calculations
# Create a function that receives three parameters, calculates a result
# depending on the given operator, and returns it. Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers.
# The operator can be one of the following:  "multiply", "divide", "add", and "subtract".

def kalkulator (komanda, broj1, broj2):
    if komanda == "multiply":
        rezultat = broj1 * broj2
    elif komanda == "divide":
        rezultat = broj1 // broj2 # ili int(broj1/broj2)
    elif komanda == "add":
        rezultat = broj1 + broj2
    elif komanda == "subtract":
        rezultat = broj1 - broj2
    return rezultat

komanda = input()
broj1 = int(input())
broj2 = int(input())
print(kalkulator(komanda, broj1, broj2))