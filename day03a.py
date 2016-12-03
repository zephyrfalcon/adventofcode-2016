# day03a.py

def is_possible_triangle(a, b, c):
    return a + b > c \
       and b + c > a \
       and c + a > b

with open("input03.txt") as f:
    lines = f.readlines()

count = 0
while lines:
    chunk, lines = lines[:3], lines[3:]
    chunk = [list(map(int, s.split())) for s in chunk]
    all_sides = list(zip(*chunk))  # transpose
    for sides in all_sides:
        if is_possible_triangle(*sides):
            count += 1

print(count)

