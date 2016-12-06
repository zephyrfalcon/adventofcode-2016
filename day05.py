# day05.py

import hashlib

def find_hash(password, index=0):
    while True:
        # Python 3's stupid Unicode/string dichotomy makes this a lot harder
        # than it used to be... >.<
        hash = hashlib.md5(password + str(index).encode('ascii'))
        digest = hash.hexdigest()
        if digest.startswith('00000'):
            return digest[5], index
        index += 1

index = 0
for i in range(8):
    c, index = find_hash(b'wtnhxymk', index)
    print(c)
    index += 1


