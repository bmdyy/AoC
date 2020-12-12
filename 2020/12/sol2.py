#!/usr/bin/python
import math

directions = [d.rstrip() for d in open("input","r")]

NORTH = 0
EAST = 90
SOUTH = 180
WEST = 270

x = 0 # ship pos
y = 0 # ship pos
wx = 10 # waypoint pos (relative)
wy = 1 # waypoint pos  (relative)
a = EAST

for d in directions:
    cmd, val = d[:1], int(d[1:])
    
    # direction commands
    if cmd == "N":
        wy += val

    elif cmd == "E":
        wx += val

    elif cmd == "S":
        wy -= val

    elif cmd == "W":
        wx -= val

    # rotate
    elif cmd == "L":
        while val > 0:
            ty = wy
            wy = wx
            wx = -ty
            val -= 90

    elif cmd == "R":
        while val > 0:
            ty = wy
            wy = -wx
            wx = ty
            val -= 90

    # forward
    elif cmd == "F":
        x += wx*val 
        y += wy*val

    print cmd,val,'-',x,y,a

print "task_1:", abs(x) + abs(y)
