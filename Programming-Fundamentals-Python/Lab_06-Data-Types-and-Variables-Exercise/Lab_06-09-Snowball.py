# 9. Snowballs
# Tony and Andi love playing in the snow and having snowball fights,
# but they always argue about who makes the best snowballs.
# They have decided to involve you in their fray by writing a program that calculates snowball data and outputs the best snowball value.
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.

# On the following lines, you will receive 3 inputs for each snowball:
# The weight of the snowball (integer).
# The time needed for the snowball to get to its target (integer).
# The quality of the snowball (integer).

# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.

# Input
# On the first input line, you will receive N – the number of snowballs.
# On the next N*3 input lines, you will be receiving data about each snowball.

# Output
# You need to print the highest calculated snowball's value in the format:
# "{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"

# Constraints
# The number of snowballs (N) will be an integer in the range [0, 100].
# The weight is an integer in the range [0, 1000].
# The time is an integer in the range [1, 500].
# The quality is an integer in the range [0, 100].

while True:
    try:
        n = int(input())
        if 0 <= n <= 100:
            break
        else:
            print("Broj nije u opsegu od 0 do 100. Pokušajte ponovo")
    except ValueError:
        print("Unos nije validan broj. Pokušajte ponovo")
snowball_value = 0
for n in range(1, n+1):
    while True:
        try:
            snowball_weight = int(input())
            if 0 <= snowball_weight <= 1000:
                break
            else:
                print("Broj nije u opsegu od 0 do 1000. Pokušajte ponovo")
        except ValueError:
            print("Unos nije validan broj. Pokušajte ponovo")
    while True:
        try:
            snowball_time = int(input())
            if 1 <= snowball_time <= 500:
                break
            else:
                print("Broj nije u opsegu od 1 do 500. Pokušajte ponovo")
        except ValueError:
            print("Unos nije validan broj. Pokušajte ponovo")
    while True:
        try:
            snowball_quality = int(input())
            if 0 <= snowball_quality <= 100:
                break
            else:
                print("Broj nije u opsegu od 0 do 100. Pokušajte ponovo")
        except ValueError:
            print("Unos nije validan broj. Pokušajte ponovo")
    value = (snowball_weight / snowball_time) ** snowball_quality
    if value > snowball_value:
        max_weight = snowball_weight
        max_time = snowball_time
        max_quality = snowball_quality
        snowball_value = value
print(f"{max_weight} : {max_time} = {int(snowball_value)} ({max_quality})")