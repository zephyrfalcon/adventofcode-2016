# day02a.py

# Just pretend that new buttons are numbered 10, 11, etc. It so happens that
# they mapto hexadecimal values. :) Convert at the end to get the button
# label.

def move_left(n):
    if n in [1, 2, 5, 10, 13]: return n
    return n - 1
def move_right(n):
    if n in [1, 4, 9, 12, 13]: return n
    return n + 1
def move_up(n):
    if n in [1, 2, 4, 5, 9]: return n
    if n in [3, 13]: return n - 2
    if n in [6, 7, 8, 10, 11, 12]: return n - 4
def move_down(n):
    if n in [5, 9, 10, 12, 13]: return n
    if n in [1, 11]: return n + 2
    if n in [2, 3, 4, 6, 7, 8]: return n + 4

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
    button = process_moves(5, line)
    print(hex(button).upper()[-1])

