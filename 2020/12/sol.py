#!/usr/bin/python
import math

directions = [d.rstrip() for d in open("input","r")]

NORTH = 0
EAST = 90
SOUTH = 180
WEST = 270

x = 0
y = 0
a = EAST

for d in directions:
    cmd, val = d[:1], int(d[1:])
    
    # direction commands
    if cmd == "N":
        y += val

    elif cmd == "E":
        x += val

    elif cmd == "S":
        y -= val

    elif cmd == "W":
        x -= val

    # rotate
    elif cmd == "L":
        a = (a - val) % 360
    elif cmd == "R":
        a = (a + val) % 360

    # forward
    elif cmd == "F":
        x += val if (a == EAST) else (-val if a == WEST else 0)
        y += val if (a == NORTH) else (-val if a == SOUTH else 0)

    print cmd,val,'-',x,y,a

print "task_1:", abs(x) + abs(y)
