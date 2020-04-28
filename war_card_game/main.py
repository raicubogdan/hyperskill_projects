# War card game - Python program that simulates a game of
# War played against a computer. 

# The purpose of this program is to touch all limit situations,
# which are quite complex to express in code. Every turn is described
# in detail order to show how the code works. Check comments and
# docstrings for more information.

import random
import time
from functions import shuffle_deck, get_rank, war, win, finish, crd_id
from models import Player, Hand, deck

while True:
    # Instantiating Player class
    shuffle_deck(deck)
    print('--War card game--\n')
    
    name1 = input('Player 1 name: ')

    player1 = Player(name1)
    player1.hand = Hand(deck[:26])

    computer = Player('Computer')
    computer.hand = Hand(deck[26:])

    game_won = False

    while not game_won:        
        action = input(f'\n{player1.name}, type anything to play a card: ')

        if action:
            # Playing and comparing cards by rank
            card1 = player1.hand.play()
            rank1 = get_rank(card1)
            print(f'\n{player1.name} played [{card1}] rank: {rank1}')

            card2 = computer.hand.play()
            rank2 = get_rank(card2)
            print(f'{computer.name} played [{card2}] rank: {rank2}\n')


            if rank1 == rank2:
                war(player1, computer, crd_id)

            elif rank1 > rank2:
                win(player1, computer, card2)

            elif rank1 < rank2:
                win(computer, player1, card1)

            # Monitoring deck changes in terminal
            print(f"\n{player1.name}'s deck\n{player1.hand.deck}")
            print(f"{player1.name}'s deck lenght: {len(player1.hand.deck)}")
            print(f"\n{computer.name}'s deck\n{computer.hand.deck}")
            print(f"{computer.name}'s deck lenght: {len(computer.hand.deck)}")

            # Win check
            if len(computer.hand.deck) == 0:
                game_won = finish(player1)
            elif len(player1.hand.deck) == 0:
                game_won = finish(computer)
