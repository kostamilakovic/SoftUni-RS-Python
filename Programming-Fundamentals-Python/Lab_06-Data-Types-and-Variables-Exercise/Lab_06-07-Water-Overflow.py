# 7. Water Overflow
# You have a water tank with a capacity of 255 liters.
# On the first line, you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive liters of water (integers), which you should pour into your tank.

# Verzija 1 - stampanje poruka tokom izvrsenja programa

capacity = 255
n = int(input())
tank = 0
for i in range(n):
    refill = int(input())
    if (tank + refill) <= capacity:
        tank += refill
    else:
        print("Insufficient capacity!")
print(tank)

# Verzija 2 - stampanje poruka nakon izvrsenja programa

# capacity = 255
# n = int(input())
# tank = 0
# messages = []
# for i in range(n):
#     refill = int(input())
#     if (tank + refill) <= capacity:
#         tank += refill
#     else:
#         messages.append("Insufficient capacity!")
# for message in messages:
#     print(message)
# print(tank)