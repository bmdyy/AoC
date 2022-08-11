#!/usr/bin/python
import hashlib
import sys

# handle args
if len(sys.argv) != 2:
    exit()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    exit()

def md5(i):
    for k in range(2017 if TASK == 2 else 1):
        m = hashlib.md5()
        m.update(str(i))
        i = m.hexdigest()
    return i

def all_equal(a, ch=None):
    base = a[0] if not ch else ch
    for i in a:
        if i != base:
            return False
    return True

def has_n_rep(key, n, ch=None):
    # look for any char repeating n times
    for i in range(0, len(key)-(n-1)):
        c = []
        for j in range(i, i+n):
            c.append(key[j])
        if all_equal(c,ch):
            return c[0]
    return False

def is_valid_key(key, salt, index):
    # p1 - check if this key has
    # 3 repeating chars (n) in a row
    n = has_n_rep(key, 3)

    # if no repeating key, it is
    # an invalid key
    if not n:
        return False

    # now check for p_2 ( one of 
    # the next 1000 HASHES has 5 n's in a row)
    for i in range(1000):
        h = md5(salt + str(index+i+1))

        if has_n_rep(h, 5, n):
            return True

    return False

def next_key(salt, index):
    index += 1
    while True:
        hd = md5(salt + str(index))
        
        if is_valid_key(hd, salt, index):
            return (hd, index)
        else:
            index += 1

# =-=-=-=-
# pretty slow
# =-=-=-=-

salt = "jlmsuwbz" # puzzle input
index = 0

for i in range(64):
    key, index = next_key(salt, index)
    print i,index,key

print index
