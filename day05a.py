# day05a.py

import hashlib

def find_hash(password, index=0):
    while True:
        # Python 3's stupid Unicode/string dichotomy makes this a lot harder
        # than it used to be... >.<
        hash = hashlib.md5(password + str(index).encode('ascii'))
        digest = hash.hexdigest()
        if digest.startswith('00000'):
            return digest[5], digest[6], index
        index += 1

positions_filled = {}
index = 0
while True:
    pos, c, index = find_hash(b'wtnhxymk', index)
    if pos > '7':
        print("Invalid position at %d (%s); ignored" % (index, pos))
    elif pos in positions_filled:
        print("Already got position at %d (%s); ignored" % (index, pos))
    else:
        print("Position %s: %s" % (pos, c))
        positions_filled[pos] = c
        if len(positions_filled) == 8:
            break
    index += 1

for i in "01234567":
    print(positions_filled[i])
