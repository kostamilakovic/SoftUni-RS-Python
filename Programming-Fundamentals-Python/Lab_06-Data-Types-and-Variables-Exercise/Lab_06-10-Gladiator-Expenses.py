# 10. Gladiator Expenses
# As a gladiator, Peter needs to repair his broken equipment when he loses a fight.
# His equipment consists of a helmet, a sword, a shield, and armor.
# You will receive Peter's lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield breaks, his armor also needs to be repaired.
# You will receive the price of each item in his equipment.
# Calculate his expenses for the year for renewing his equipment.

# Input / Constraints
# The input will consist of 5 lines:
# On the first line, you will receive the lost fights count – an integer in the range [0, 1000].
# On the second line, you will receive the helmet price - a floating-point number in the range [0, 1000].
# On the third line, you will receive the sword price - a floating-point number in the range [0, 1000].
# On the fourth line, you will receive the shield price - a floating-point number in the range [0, 1000].
# On the fifth line, you will receive the armor price - a floating-point number in the range [0, 1000].

# Output
# As output, you must print Peter`s total expenses for new equipment:
# "Gladiator expenses: {expenses} aureus"

expenses = 0
while True:
    try:
        lost_fights_count = int(input())
        if 0 <= lost_fights_count <= 1000:
            break
        else:
            print("Broj nije u opsegu od 0 do 100. Pokušajte ponovo")
    except ValueError:
        print("Unos nije validan broj. Pokušajte ponovo")
while True:
    try:
        helmet_price = float(input())
        if 0 <= helmet_price <= 1000:
            break
        else:
            print("Broj nije u opsegu od 0 do 100. Pokušajte ponovo")
    except ValueError:
        print("Unos nije validan broj. Pokušajte ponovo")
while True:
    try:
        sword_price = float(input())
        if 0 <= sword_price <= 1000:
            break
        else:
            print("Broj nije u opsegu od 0 do 100. Pokušajte ponovo")
    except ValueError:
        print("Unos nije validan broj. Pokušajte ponovo")
while True:
    try:
        shield_price = float(input())
        if 0 <= shield_price <= 1000:
            break
        else:
            print("Broj nije u opsegu od 0 do 100. Pokušajte ponovo")
    except ValueError:
        print("Unos nije validan broj. Pokušajte ponovo")
while True:
    try:
        armor_price = float(input())
        if 0 <= armor_price <= 1000:
            break
        else:
            print("Broj nije u opsegu od 0 do 100. Pokušajte ponovo")
    except ValueError:
        print("Unos nije validan broj. Pokušajte ponovo")
for lost_fight in range(1, lost_fights_count+1):
    if lost_fight % 2 == 0:
        expenses += helmet_price
    if lost_fight % 3 == 0:
        expenses += sword_price
    if lost_fight % 6 == 0:
        expenses += shield_price
    if lost_fight % 12 == 0:
        expenses += armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")