# Stage 1. Setting up the game
import random

status_players = ['player', 'computer']
stock_total = [[n, m] for n in range(0, 7) for m in range(n, 7)]
snakes = [[n, n] for n in range(0, 7)]
snakes.reverse()
random.seed()
random.shuffle(stock_total)

domino_snake = []
stock_pieces = [n for n in stock_total[0:14]]
player_pieces = [n for n in stock_total[14:21]]
cpu_pieces = [n for n in stock_total[21:28]]

for start_piece in snakes:
    if start_piece in player_pieces:
        status = 'computer'
        domino_snake.append(start_piece)
        player_pieces.remove(start_piece)
        break

    if start_piece in cpu_pieces:
        status = 'player'
        domino_snake.append(start_piece)
        cpu_pieces.remove(start_piece)
        break

print(f'Stock pieces: {stock_pieces}')
print(f'Computer pieces: {cpu_pieces}')
print(f'player pieces: {player_pieces}')
print(f'Domino snake: {domino_snake}')
print(f'Status: {status}')
