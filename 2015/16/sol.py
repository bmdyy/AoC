#!/usr/bin/python
import sys

# handle args
if len(sys.argv) != 2:
    exit()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    exit()

# stats of the sue we are looking for
looking_for = {
    'children':'3',
    'cats': '7',
    'samoyeds': '2',
    'pomeranians': '3',
    'akitas': '0',
    'vizslas': '0',
    'goldfish': '5',
    'trees': '3',
    'cars': '2',
    'perfumes': '1'
}

def info_matches(i, lf):
    # loop through keys of info, and
    # see if they all match the values
    # in looking for, for the respective
    # key names
    for k in i:
        # TASK 1
        if TASK == 1:
            if lf[k] != i[k]:
                return False
        # TASK 2
        else:
            if k in ['cats', 'trees']:
                # greater than
                if lf[k] > i[k]:
                    return False
            elif k in ['pomeranians','goldfish']:
                # less than
                if lf[k] < i[k]:
                    return False
            else:
                # equal to
                if lf[k] != i[k]:
                    return False

    return True

# loop through the file
f = open("input", "r")
for line in f:
    tk = [t.replace(':','').replace(',','') for t in line.rstrip().split(" ")]
    # format:
    # 0> 'Sue'  1> Sue #
    # 2> key 1  3> val 1
    # 4> key 2  5> val 2
    # 6> key 3  7> val 3

    sue_num = tk[1]

    # info we know about this sue
    info = {
        tk[2]: tk[3],
        tk[4]: tk[5],
        tk[6]: tk[7]
    }

    # check if this info is a subset
    # of looking_for
    if info_matches(info, looking_for):
        print sue_num

f.close()
