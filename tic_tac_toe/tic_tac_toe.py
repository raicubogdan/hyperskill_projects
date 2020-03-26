# A scalable game of tic-tac-toe with interface
# This program is inspired by the tic-tac-toe game
# from https://pythonprogramming.net/introduction-learn-python-3-tutorials/

import itertools  # Used to cycle between players

def win(game):
    """Win conditions"""
    # Vertical win condition
    for idx, _ in enumerate(game):
        col = []
        for row in game:
            col.append(row[idx])
        if col.count(col[0]) == len(col) and col[0] != 0:
            print(f'{col[0]} wins vertically!')
            return True

    # Horizontal win condition
    for row in game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f'{row[0]} wins horizontally')
            return True

    # Diagonal win condition
    diags = []
    for idx, _ in enumerate(game):
        diags.append(game[idx][idx])

    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f'{diags[0]} wins diagonally!(\\)')
        return True

    diags = []
    for idx, reverse_idx in enumerate(range(len(game))):
        diags.append(game[idx][reverse_idx])

    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f'{diags[0]} wins diagonally! (/)')
        return True

def game_board(game_map, row, column, player):
    """Displays the game board and writes down
    players choices"""

    try:
        if game_map[row][column] != 0:
            print('That position is occupied! Choose another one: ')
            return False

        game_map[row][column] = player

        # Game interface
        col_names = [str(i) for i in range(len(game_map))]
        columns = '     ' + '  '.join(col_names)
        print(columns)
        print('  ' + '-'*len(columns))
        for idx, row in enumerate(game_map):
            print(f'{idx} | ', end = '')
            for idx, _ in enumerate(game_map):
                if row[idx] == 0:
                    print(f'   ', end = '')
                else:
                    print(f'{row[idx]}  ', end = '')
            print('|')
        print('  ' + '-'*len(columns))
        
        return game_map

    except IndexError:
        print('Not a valid position')
        return False

while True:
    players = ['X', 'O']
    player_choice = itertools.cycle(players)
    game_won = False #Trigger for replay

    game_size = int(input('Size of game in rows and columns: '))
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    while not game_won:
        player = next(player_choice)
        print(f"\nPlayer {player} turn")
        played = False

        while not played: # Writing down choice
            row = int(input('Plase choose a row: '))
            column = int(input('Plesa choose a column: '))
            played = game_board(game, row, column, player)

            if win(game):
                choice = input(('Do you wanna play again? (y/n)'))
                if choice == 'y':
                    game_won = True
                else:
                    exit()
