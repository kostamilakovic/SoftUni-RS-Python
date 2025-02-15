# 5. Special Numbers
# Write a program that reads an integer n.
# Then, for all numbers in the range [1, n], print the number
# and if it is special or not (True / False).
# A number is special when the sum of its digits is 5, 7, or 11.

# Verzija 1

n = int(input())
for i in range (1,n+1): # iteriramo kroz sve cifre broja n
    sum = 0 # resetuje sumu cifara na 0 na pocetku svake iteracije
    num = i # promenjivoj num dodeljujemo vrednost "i" koju iteriramo
    while num > 0: # petlja ce se ponavljati dok broj ne svedemo na 0
        sum += num % 10 # suma se uvecava za ostatak deljenja sa 10
        num = int(num/10) # pretvaranje float u int brise sve posle zareza
    if sum == 5 or sum == 7 or sum == 11: # proveravamo da li je broj specijalan
        print(f"{i} -> True sum = {sum}") # ukoliko jeste stampamo poruku True
    else:
        print(f"{i} -> False sum = {sum}") # ukoliko nije stampamo poruku False
print(f"{int(3579/10)}")