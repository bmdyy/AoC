#!/usr/bin/python
import sys
import math

# handle args
TASK = 1
if len(sys.argv) != 2:
    exit()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    exit()

# open file
f = open("input", "r")

# convert to coordinates and count steps
wires = []
for line in f:
    cx = 0
    cy = 0
    steps = 0
    wire = [[cx,cy,steps]]

    for move in line.rstrip().split(","):
        direction = move[0]
        val = int(move[1:])
        if direction == 'R':
            cx += val
        elif direction == 'L':
            cx -= val
        elif direction == 'U':
            cy += val
        else:
            cy -= val
        steps += val
        wire.append([cx,cy,steps])

    wires.append(wire)

# 2d distance between two points
def dist(a,b):
    return math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)

# a0: point a of wire 0
# b0: point b of wire 0
# c0: steps on wire 0 until point a0
# a1: point a of wire 1
# b1: point b of wire 1
# c1: steps on wire 1 until point a1
def intersect(a0,b0,c0,a1,b1,c1):
    # both vertical lines
    if a0[0] == b0[0] and a1[0] == b1[0]:
        return None
    # both horizontal lines
    elif a0[1] == b0[1] and a1[1] == b1[1]:
        return None
    # one horizontal, one vertical
    elif (a0[1] == b0[1] and a1[0] == b1[0]) or (a0[0] == b0[0] and a1[1] == b1[1]):
        # check which wire is the horizontal
        # one and which one is the vertical
        # wire
        h0 = None
        h1 = None
        v0 = None
        v1 = None
        if a0[1] == b0[1]:
            h0 = a0
            h1 = b0
            v0 = a1
            v1 = b1
        else:
            h0 = a1
            h1 = b1
            v0 = a0
            v1 = b0

        # for there to be an intersection,
        # v must be between h's x vals
        if (v0[0] > h0[0]) and (v0[0] < h1[0]):
            # if v is running vertically 
            # between h's x0 and x1, then 
            # v crosses if the y's go below
            # and above
            if min(v0[1], v1[1]) < h0[1] and max(v0[1], v1[1]) > h0[1]:
                # they cross!
                itrs = [v0[0], h0[1]]
                # calculate total steps
                s_w0 = c0 + int(dist(a0, itrs))
                s_w1 = c1 + int(dist(a1, itrs))
                # return intersection point + 
                # total steps taken
                return [itrs[0], itrs[1], s_w0 + s_w1]
            else:
                return None
        else:
            return None

# loop through all lines
intersections = []
for i in range(len(wires[0])-1):
    a0 = wires[0][i]
    b0 = wires[0][i+1]
    c0 = wires[0][i][2]

    for j in range(len(wires[1])-1):
        a1 = wires[1][j]
        b1 = wires[1][j+1]
        c1 = wires[1][j][2]

        # check for interesections
        c = intersect(a0,b0,c0,a1,b1,c1)
        if c:
            intersections.append(c)

print intersections

# find closest intersection to port
if TASK == 1:
    closest = 999999999
    for itr in intersections:
        d = abs(itr[0]) + abs(itr[1])
        if d < closest:
            closest = d
    print closest

# find intersection with fewest steps
else:
    least_steps = 999999999
    for itr in intersections:
        s = itr[2]
        if s < least_steps:
            least_steps = s
    print least_steps

f.close()
