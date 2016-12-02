# day01.py

# which direction are we facing if we turn left/right once?
TURN_RIGHT = {"N": "E", "E": "S", "S": "W", "W": "N"}
TURN_LEFT = {"N": "W", "W": "S", "S": "E", "E": "N"}

with open("input01.txt") as f:
    data = f.read()

parts = data.split()
directions = [p.rstrip(",") for p in parts] # remove trailing commas

curr_dir = "N"
x, y = (0, 0)

for d in directions:
    left_right, times = d[0], int(d[1:])
    if left_right == 'R':
        curr_dir = TURN_RIGHT[curr_dir]
    else:
        curr_dir = TURN_LEFT[curr_dir]
    if curr_dir == 'N':
        y = y + times
    elif curr_dir == 'S':
        y = y - times
    elif curr_dir == 'E':
        x = x + times
    elif curr_dir == 'W':
        x = x - times

distance = abs(x) + abs(y)
print("distance:", distance)

