# day07.py

import re

re_ipv7 = re.compile("(\[.*?\])")

def has_abba(s):
    for i in range(len(s)-4+1):
        chunk = s[i:i+4]
        if chunk[0] != chunk[1] and chunk[0] == chunk[3] and chunk[1] == chunk[2]:
            return True
    return False

def find_abas(s):
    abas = []
    for i in range(len(s)-3+1):
        chunk = s[i:i+3]
        if chunk[0] != chunk[1] and chunk[0] == chunk[2]:
            abas.append(chunk)
    return abas

def supports_ssl(ipv7):
    parts = re_ipv7.split(ipv7)
    abas = []
    babs = []
    for part in parts:
        if part.startswith('['):
            babs.extend(find_abas(part))
        else:
            abas.extend(find_abas(part))
    
    for aba in abas:
        bab = aba[1] + aba[0] + aba[1] # "aba" => "bab"
        if bab in babs:
            return True
    return False

with open("input07.txt") as f:
    lines = f.readlines()

ok = [line for line in lines if supports_ssl(line)]
print(len(ok))

