# day09.py

import re
import string

re_marker = re.compile("\((\d+)x(\d+)\)")

def decompress(s):
    result = ""
    while s:
        m = re_marker.search(s)
        if m:
            num_chars, times = int(m.group(1)), int(m.group(2))
            start, end = m.span()
            result += s[:start] # add text before marker
            s = s[end:] # remove marker text
            chunk = s[:num_chars]
            result += (chunk * times)
            s = s[num_chars:]
        else:
            # there's no marker, just add all text as-is
            result += s
            break
    return result

with open("input09.txt") as f:
    data = f.read()

data = ''.join([c for c in data if not c in string.whitespace])

print(len(decompress(data)))
