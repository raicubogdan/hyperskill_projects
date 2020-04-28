import random
import time
from models import hierarchy

# 'crd_id': Value used in limit situations when two or more wars occur consequently.
# It gets incremented by 3 after each consequent war to add another 3 cards
# in the play. Check war() function.
crd_id = 0

def finish(winner):
    """
    Stating winner and asking for replay.
    """
    choice = input(f'{winner.name} Won!\nPlay again? (y/n)')
    if choice == 'y':
        return True
    else:
        exit()

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def get_rank(card):
    """
    Rank by which cards are compared.
    """
    for idx, rank in enumerate(hierarchy):
        if card in rank:
            return idx

def win(winner, loser, card):
    """
    Round winner.
    """
    print(f'{winner.name} wins {card} from {loser.name}.')
    winner.hand.deck.append(loser.hand.deck.pop(0))
    winner.hand.deck.append(winner.hand.deck.pop(0))

def war_win(winner, loser, crd_id, win_card, win_rank, lose_card, lose_rank):
    """
    Determines war winner if ranks differ.
    """
    print(f'{winner.name} plays {win_card}(rank {win_rank}) and wins '
          f'{loser.hand.deck[:4 + crd_id]} against {loser.name}\'s '
          f'{lose_card}(rank {lose_rank})')

    bottom = loser.hand.deck[:4 + crd_id] + winner.hand.deck[:4 + crd_id]
    loser.hand.deck = loser.hand.deck[4 + crd_id:]
    winner.hand.deck = winner.hand.deck[4 + crd_id:]
    [winner.hand.deck.append(i) for i in bottom]

def war(player1, computer, crd_id):
    """
    Checks deck's lenght, gets card ranks, compares card ranks.
    If ranks are identical, the function is called again recursively.
    """
    print('War!')
    print('Both players lay the top three cards of their decks...')
    time.sleep(2)
    
    # In a war, if deck's lenght is less than 4,
    # all the rest of the cards will be played
    if len(player1.hand.deck) < 4 + crd_id:
        third1 = player1.hand.deck
    else:
        third1 = player1.hand.deck[3 + crd_id]

    if len(computer.hand.deck) < 4 + crd_id:
        third2 = computer.hand.deck
    else:
        third2 = computer.hand.deck[3 + crd_id]

    third_rank1 = get_rank(third1)
    third_rank2 = get_rank(third2)

    if third_rank1 > third_rank2:
        war_win(player1, computer, crd_id, third1, third_rank1, third2, third_rank2)

    elif third_rank1 < third_rank2:
        war_win(computer, player1, crd_id, third2, third_rank2, third1, third_rank1)

    elif third_rank1 == third_rank2:
        crd_id += 3
        war(player1, computer, crd_id)
