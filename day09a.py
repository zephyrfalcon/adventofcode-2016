# day09a.py

import re
import string

re_marker = re.compile("\((\d+)x(\d+)\)")

def decompressed_length(s):
    length = 0
    while s:
        m = re_marker.search(s)
        if m:
            num_chars, times = int(m.group(1)), int(m.group(2))
            start, end = m.span()
            length += start # add text before marker
            s = s[end:] # remove marker text
            chunk = s[:num_chars]
            dl = decompressed_length(chunk)
            length += (dl * times)
            s = s[num_chars:]
        else:
            # there's no marker, just add all text as-is
            length += len(s)
            break
    return length

with open("input09.txt") as f:
    data = f.read()

data = ''.join([c for c in data if not c in string.whitespace])

print(decompressed_length(data))
