# 3. Football Cards
# You are up to handle the referee's little notebook
# and count the players who were sent off for fouls and misbehavior.
# The rules: # Two teams, named "A" and "B" have 11 players each.
# The players on each team are numbered from 1 to 11.
# Any player may be sent off the field by being given a red card.
# If one of the teams has less than 7 players remaining,
# the referee stops the game immediately, and the team with less than 7 players loses.
# The card is a string with the team's letter ("A" or "B")
# followed by a single dash and the player's number. e.g.,
# the card "B-7" means player #7 from team B received a card.
# The task: You will be given a sequence of cards (could be empty),
# separated by a single space. You should print the count of
# remaining players on each team at the end of the game
# in the format: "Team A - {players_count}; Team B - {players_count}".
# If the referee terminated the game, print an additional line: "Game was terminated".

# Note for the random tests:
# If a player who has already been sent off receives another card - ignore it.

linija = input() # A-1 A-5 A-10 B-2
kartoni = linija.split(" ") # ["A-1", "A-5", "A-10", "B-2"]
timA = [1,2,3,4,5,6,7,8,9,10,11] # nacin 1
timB = list(range(1, 12)) # nacin 2 (bolji nacin)
for karton in kartoni:
    tim = karton[0] # iz svakog kartona izdvajamo pocetno slovo
    broj = int(karton[2:]) # iz svakog kartona izdvajamo broj igraca
    if tim == "A":
        if broj in timA: # ako je karton glasio na tim A i broj igraca se nalazi u timu A
            timA.remove(broj) # uklanjamo broj igraca iz tima B
            if len(timA) < 7:
                break
    elif tim == "B":
        if broj in timB: # ako je karton glasio na tim B i broj igraca se nalazi u timu B
            timB.remove(broj) # uklanjamo broj igraca iz tima B
            if len(timB) < 7:
                break
print(f"Team A - {len(timA)}; Team B - {len(timB)}")
if len(timA) < 7 or len(timB) < 7:
    print("Game was terminated")