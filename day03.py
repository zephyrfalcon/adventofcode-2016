# day03.py

def is_possible_triangle(a, b, c):
    return a + b > c \
       and b + c > a \
       and c + a > b

with open("input03.txt") as f:
    lines = f.readlines()

count = 0
for line in lines:
    parts = line.split()
    sides = map(int, parts)
    if is_possible_triangle(*sides):
        count += 1

print(count)

