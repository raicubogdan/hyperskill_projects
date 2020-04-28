# SUITE and RANKS are used to create the
# 52 cards of a standard deck
SUITE = 'H D S C'.split()
RANKS = '2 3 4  5 6 7 8 9 10 J Q K A'.split()

deck = []
hierarchy = []

for i in RANKS: # Creating a deck of 52 cards ('deck' variable)
    for j in SUITE:
        deck.append(i+j)

for i in RANKS: # Creating ranks for card comparison ('hierarchy' variable)
        hierarchy.append([i + j for j in SUITE])

class Hand: 
    def __init__(self, deck):
        self.deck = deck

    def play(self):
        """Plays the first card of the deck"""
        return self.deck[0]

class Player:
    def __init__(self, name):
        self.hand = None
        self.name = name
