#!/usr/bin/python
import sys

if len(sys.argv) != 2:
    exit()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    exit()

p_range = [int(i) for i in "145852-616942".split('-')]

num_valid = 0
# loop through range
for p in range(p_range[0], p_range[1]+1):
    # property 1 and 2 are trivial
    # property 3 - two adj digits are ident.
    pr_3 = False
    # property 4 - never decrease going ltr
    pr_4 = True

    last_d = p % 10
    p /= 10

    c_group_size = 1
    while p > 0:
        d = p % 10
       
        # property 3
        if last_d == d:
            c_group_size += 1
        else:
            if (TASK == 1 and c_group_size > 1) or \
                    (TASK == 2 and c_group_size == 2):
                pr_3 = True
            c_group_size = 1

        # property 4
        if last_d < d:
            pr_4 = False

        p /= 10
        last_d = d

    # check for groups including
    # the very first digit
    if (TASK == 1 and c_group_size > 1) or \
            (TASK == 2 and c_group_size == 2):
        pr_3 = True

    if pr_3 and pr_4:
        num_valid += 1

print num_valid
