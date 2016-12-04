# day04.py

import collections
import string

def split_line(s):
    idx = s.find('[')
    blurb, checksum = s[:idx], s[idx+1:idx+6]
    sector_id = int(blurb.split('-')[-1])
    return blurb, sector_id, checksum

def shift_letter(letter, shift):
    x = ord(letter)
    if not (97 <= x <= 122):  # not a letter, return unchanged
        return letter
    shift = shift % 26  # only 26 possibilities
    x = x + shift
    if x > 122: x = x - 26  # wrap around
    return chr(x)

def decrypt_name(name, sector_id):
    q = [shift_letter(c, sector_id) for c in name]
    return ''.join(q)

with open("input04.txt") as f:
    lines = f.readlines()

for line in lines:
    blurb, sector_id, checksum = split_line(line)
    real_name = decrypt_name(blurb, sector_id)
    print(real_name)
    if 'north' in real_name: break
    # this just stops at the first name that contains 'north', which happens
    # to work in this case :3

