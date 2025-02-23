# 5. Faro Shuffle
# A faro shuffle is a method for shuffling a deck of cards,
# in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved,
# such that the original bottom card is still on the bottom
# and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six']
# once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space)
# and on the second line receives a count of faro shuffles that should be made.
# Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.

# Verzija 1

cards = input()
shuffles = int(input())
deck = cards.split()
split = len(deck)//2

for n in range(shuffles):
    new_deck = []
    deck_1 = deck[:split]
    deck_2 = deck[split:]
    for m in range(split):
        new_deck.append(deck_1[m])
        new_deck.append(deck_2[m])
    deck=new_deck
print(deck)

# Verzija 2 - posto su prva i zadnja karta iste, mozemo da dodamo prvu kartu, izmesamo karte izmedju prve i poslednje i dodamo poslednju

cards = input()
shuffles = int(input())
deck = cards.split()
split = len(deck)//2

for n in range(shuffles):
    new_deck = []
    deck_1 = deck[:split]
    deck_2 = deck[split:]
    for m in range(split):
        new_deck.append(deck_1[m])
        new_deck.append(deck_2[m])
    deck=new_deck
print(deck)