#!/usr/bin/python
import sys

# handle args
if len(sys.argv) != 2:
    exit()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    exit()

def reversed_polarity(atom):
    return atom.swapcase()

def simulate(poly):
    i = 0
    while i < len(poly)-1:
        if poly[i] == reversed_polarity(poly[i+1]):
            poly = poly[:i] + poly[i+2:]
            i = 0
        else:
            i += 1
    return poly

def get_types(poly):
    types = []
    for t in poly:
        if (t not in types) and \
                (reversed_polarity(t) not in types):
            types.append(t)
    return types

def remove_type(poly, t):
    new_poly = ""
    for c in poly:
        if c == t or c == reversed_polarity(t):
            continue
        else:
            new_poly += c
    return new_poly


# read input
f = open("input","r")
polymer = f.readline().rstrip()
f.close()

if TASK == 1:
    print len(simulate(polymer))

elif TASK == 2:
    types = get_types(polymer)
    print 'Types:', ",".join(types)
    shortest = sys.maxint
    for t in types:
        tmp = remove_type(polymer, t)
        s = simulate(tmp)
        if len(s) < shortest:
            shortest = len(s)
        print t,'--',len(s)
    print shortest

