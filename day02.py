# day02.py

def move_left(n):
    if n in [1, 4, 7]: return n
    return n - 1
def move_right(n):
    if n in [3, 6, 9]: return n
    return n + 1
def move_up(n):
    if n in [1, 2, 3]: return n
    return n - 3
def move_down(n):
    if n in [7, 8, 9]: return n
    return n + 3

MOVES = {'U': move_up, 'D': move_down, 'L': move_left, 'R': move_right}

def process_moves(button, moves):
    for move in moves:
        f = MOVES.get(move, None)
        if f:
            button = f(button)
    return button

with open("input02.txt") as f:
    lines = f.readlines()

for line in lines:
    #print(line)
    button = process_moves(5, line)
    print(button)

