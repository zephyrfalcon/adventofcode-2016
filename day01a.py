# day01a.py

# Code is kinda messy here with duplication and the exception to break out of
# things, but hey, what is a guy to do... :-)

# which direction are we facing if we turn left/right once?
TURN_RIGHT = {"N": "E", "E": "S", "S": "W", "W": "N"}
TURN_LEFT = {"N": "W", "W": "S", "S": "E", "E": "N"}

with open("input01.txt") as f:
    data = f.read()

parts = data.split()
directions = [p.rstrip(",") for p in parts] # remove trailing commas

curr_dir = "N"
x, y = (0, 0)
visited = {(x,y)}

class VisitedException(Exception): pass

def check(position):
    x, y = position
    if (x, y) in visited:
        raise VisitedException
    else:
        visited.add((x,y))

try:
    for d in directions:
        left_right, times = d[0], int(d[1:])
        if left_right == 'R':
            curr_dir = TURN_RIGHT[curr_dir]
        else:
            curr_dir = TURN_LEFT[curr_dir]
        if curr_dir == 'N':
            for i in range(times):
                y += 1
                check((x,y))
        elif curr_dir == 'S':
            for i in range(times):
                y = y - 1
                check((x,y))
        elif curr_dir == 'E':
            for i in range(times):
                x = x + 1
                check((x,y))
        elif curr_dir == 'W':
            for i in range(times):
                x = x - 1
                check((x,y))
except VisitedException:
    pass

distance = abs(x) + abs(y)
print("distance:", distance)

