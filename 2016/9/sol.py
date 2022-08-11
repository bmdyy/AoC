#!/usr/bin/python
import re
import sys

# parse args
if len(sys.argv) != 2:
    exit()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    exit()

# regex that matches markers
mk = "\([0-9]+x[0-9]+\)"

# parses a marker into [int, int]
def parse_mk(mk):
    return [int(i) for i in mk[1:-1].split("x")]

def decompress(f): 
    d_f = "" # decompressed file ( output )
    n_mk = re.search(mk, f) # first marker ( if one exists )
    while n_mk: # while there are still markers
        s = n_mk.span() # get span of match
        m = parse_mk(n_mk.group()) # parse marker info

        # next m[0] characters are to be repeated m[1] times
        # target = s[1] -- s[1] + m[0]
        t = f[s[1]:s[1]+m[0]] # get target info
        o = t * m[1] # expanded info
        d_f += f[:s[0]] + o # add part before marker to d_f
 
        f = f[s[1] + m[0]:] # cut the marker and its target
                            # data out of f

        n_mk = re.search(mk, f) # next marker
    return d_f + f

def len_decompressed_v2(f):
    n_mk = re.search(mk, f)
    l = 0 
    ls = 0
    while n_mk:
        s = n_mk.span()
        m = parse_mk(n_mk.group())
        t = f[s[1]:s[1]+m[0]]
        ls += len(f[:s[0]])
        l += m[1] * len_decompressed_v2(t)
        f = f[s[1]+m[0]:]
        n_mk = re.search(mk, f)
    if l == 0:
        return len(f)
    else:
        return ls + l + len(f)

f = open("input","r")
# TASK 1: length of decompressed data using version 1
if TASK == 1:
    print len(decompress(f.readline()).rstrip())
# TASK 2: length of decompressed data using version 2
# (without actually decompressing the data, as it will 
#  take too much memory space)
else:
    print len_decompressed_v2(f.readline().rstrip())
f.close()
