# day04.py

import collections
import string

def split_line(s):
    idx = s.find('[')
    blurb, checksum = s[:idx], s[idx+1:idx+6]
    sector_id = int(blurb.split('-')[-1])
    return blurb, sector_id, checksum

def calculate_checksum(blurb):
    d = count_letters(blurb)
    return make_checksum(d)

def count_letters(s):
    d = collections.defaultdict(lambda: 0)
    for c in s:
        if c in string.ascii_lowercase:
            d[c] += 1
    return d

def make_checksum(counts):
    values = sorted([(v, k) for (k, v) in counts.items()], 
                    key=lambda x: (-x[0], x[1]))
    first_five = [k for (v, k) in values[:5]]
    return ''.join(first_five)

with open("input04.txt") as f:
    lines = f.readlines()

total = 0
for line in lines:
    blurb, sector_id, checksum = split_line(line)
    my_checksum = calculate_checksum(blurb)
    if my_checksum == checksum:
        total += sector_id

print(total)

