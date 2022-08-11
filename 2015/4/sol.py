#!/usr/bin/python
import hashlib, sys

# handle args
if len(sys.argv) != 2:
    exit()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    exit()

def next_hash(secret, n):
    hd = "11111"
    while hd[0:(5 if TASK == 1 else 6)] != ("00000" if TASK == 1 else "000000"):
        m = hashlib.md5()
        m.update(secret + str(n))
        hd = m.hexdigest()
        n += 1
    return (n-1, hd)

secret = "ckczppom"
n = 1

print next_hash(secret, 1)
