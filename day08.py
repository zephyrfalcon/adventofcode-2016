# day08.py

import re

WIDTH, HEIGHT = 50, 6
OFF, ON = 0, 1

def rect(x, y):
    for yy in range(y):
        for xx in range(x):
            pixels[xx,yy] = ON

def rotate_row(row, offset): 
    values = [pixels[x,row] for x in range(WIDTH)]
    for i in range(offset):
        values = [values[-1]] + values[:-1]
    for x in range(WIDTH):
        pixels[x,row] = values[x]

def rotate_column(col, offset): 
    values = [pixels[col,y] for y in range(HEIGHT)]
    for i in range(offset):
        values = [values[-1]] + values[:-1]
    for y in range(HEIGHT):
        pixels[col,y] = values[y]

def count_lit_pixels():
    return len([q for q in pixels.values() if q == ON])

regexen = [
    (re.compile("rect (\d+)x(\d+)"), rect),
    (re.compile("rotate row y=(\d+) by (\d+)"), rotate_row),
    (re.compile("rotate column x=(\d+) by (\d+)"), rotate_column),
]

pixels = {}
for y in range(HEIGHT):
    for x in range(WIDTH):
        pixels[x,y] = OFF

def match_line(line):
    for (regex, f) in regexen:
        m = regex.search(line)
        if m:
            return m, f
    raise ValueError("Line does not match a regex: %r" % (line,))

def process_regex(m, f):
    values = [int(s) for s in m.groups()]
    f(*values)

with open("input08.txt") as f:
    lines = f.readlines()
for line in lines:
    m, f = match_line(line)
    process_regex(m, f)
print(count_lit_pixels())
