# day06.py

import collections

def find_most_frequent_in_dict(d):
    freqs = sorted([(freq, letter) for (letter, freq) in d.items()])
    return freqs[0]

def find_most_frequent(lines):
    length = len(lines[0])
    counts = {}
    for i in range(length):
        counts[i] = collections.defaultdict(lambda: 0)
    for line in lines:
        for idx, c in enumerate(line):
            counts[idx][c] += 1

    word = ""
    for i in range(length):
        freq, letter = find_most_frequent_in_dict(counts[i])
        word += letter

    return word

with open("input06.txt") as f:
    lines = f.readlines()

print(find_most_frequent(lines))
