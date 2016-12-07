# day07.py

import re

re_ipv7 = re.compile("(\[.*?\])")

def has_abba(s):
    for i in range(len(s)-4+1):
        chunk = s[i:i+4]
        if chunk[0] != chunk[1] and chunk[0] == chunk[3] and chunk[1] == chunk[2]:
            return True
    return False

def supports_tls(ipv7):
    found_abba = False
    parts = re_ipv7.split(ipv7)
    for part in parts:
        if part.startswith('['):
            if has_abba(part):
                return False
        else:
            if has_abba(part):
                found_abba = True
    return found_abba

with open("input07.txt") as f:
    lines = f.readlines()

ok = [line for line in lines if supports_tls(line)]
print(len(ok))

