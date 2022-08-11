#!/usr/bin/python
import sys

if len(sys.argv) != 2:
    print "usage: {} TASK".format(sys.argv[0])
    print ""
    print "TASK can be either 1 or 2"
    exit()

f = open('input','r')
entries = []

for line in f:
    line = line.rstrip()
    entries.append(int(line))
f.close()

# part 1
if sys.argv[1] == '1':
    for a in entries:
        for b in entries:
            if a+b == 2020:
                print "{} * {} = {}".format(a,b,a*b)
                exit()
elif sys.argv[1] == '2':
    # part 2
    for a in entries:
        for b in entries:
            for c in entries:
                if a+b+c == 2020:
                    print "{} * {} * {} = {}".format(a,b,c,a*b*c)
                    exit()
