#!/usr/bin/python
import sys

# handle args
if len(sys.argv) != 2:
    exit()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    exit()

f = open("input","r") # MUST END WITH NEWLINE
line = f.readline()

def t2(g, s):
    c = 0
    for i in g:
        if i==s:
            c += 1
    return c

sum_count = 0
groups = [0] * 26 # 26 letters
group_size = 0
while line != '':
    tmp = line.rstrip()
    if tmp == '':
        # new group
        sum_count += sum(groups) if TASK == 1 else \
                t2(groups, group_size)
        groups = [0] * 26
        group_size = 0

    else:
        group_size += 1
        for c in tmp:
            if TASK == 1:
                groups[ord(c)-97] = 1
            elif TASK == 2:
                groups[ord(c)-97] += 1

    line = f.readline()

print sum_count
f.close()
