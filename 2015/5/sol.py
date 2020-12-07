#!/usr/bin/python
import re

def is_nice_v1(s):
    v = {'a':0,'e':0,'i':0,'o':0,'u':0} # p_1
    p_2 = False # double chars

    for i in range(len(s)-1):
        c = s[i]
        c_next = s[i+1]

        # check for vowels
        if c in v:
            v[c] += 1

        # check for double chars
        if c == c_next:
            p_2 = True

    # check last char for vowels
    if s[-1] in v:
        v[s[-1]] += 1

    # sum up vowels
    sv = 0
    for k in v:
        sv += v[k]

    # p_3 - check for bad strs
    p_3 = re.search(r"ab|cd|pq|xy", s) == None

    # check if all conds are fullfilled
    return sv >= 3 and p_2 and p_3

def is_nice_v2(s):
    p_1 = False
    i = 0
    while i < len(s)-3:
        base = s[i:i+2]
        j = i+2
        while j < len(s)-1:
            check = s[j:j+2]
            if base == check:
                p_1 = True
            j += 1
        i += 1

    p_2 = False
    i = 0
    while i < len(s)-2:
        c0 = s[i]
        c1 = s[i+1]
        c2 = s[i+2]
        if c0 == c2:
            p_2 = True
        i += 1
    return p_1 and p_2

with open("input", "r") as f:
    count_v1 = 0
    count_v2 = 0
    for word in f:
        count_v1 += is_nice_v1(word)
        count_v2 += is_nice_v2(word)

    print "task_1:",count_v1
    print "task_2:",count_v2
