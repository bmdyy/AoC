#!/usr/bin/python
import sys

if len(sys.argv) != 2:
    exit()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    exit()

grid = [[c for c in r.rstrip()] for r in open("input","r")]

max_r = len(grid) - 1
max_c = len(grid[0]) - 1

def get_direct_neighbors(r,c):
    n = 0
    # right
    if c < max_c:
        if grid[r][c+1] == '#':
            n += 1

        # right down
        if r < max_r:
            if grid[r+1][c+1] == '#':
                n += 1

        # right up
        if r > 0:
            if grid[r-1][c+1] == '#':
                n += 1

    # left
    if c > 0:
        if grid[r][c-1] == '#':
            n += 1


        # left up
        if r > 0:
            if grid[r-1][c-1] == '#':
                n += 1  

    # down
    if r < max_r:
        if grid[r+1][c] == '#':
            n += 1

    # up
    if r > 0:
        if grid[r-1][c] == '#':
            n += 1

    return n

def get_visible_neighbors(r,c):
    # number of visible seats
    n = 0
    
    # up, up+right, right, down+right, down, down+left, left, up+left
    directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    
    for d in directions:
        r_ = r + d[0]
        c_ = c + d[1]
        while (r_ >= 0 and r_ <= max_r) and \
                (c_ >= 0 and c_ <= max_c):
            # check seat
            if grid[r_][c_] == 'L':
                break

            elif grid[r_][c_] == '#':
                n = n + 1
                break

            # move in direction
            r_ = r_ + d[0]
            c_ = c_ + d[1]

    return n

changes = -1
next_grid = [r[:] for r in grid]
while changes != 0:
    changes = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            seat = grid[r][c]

            if seat == '.':
                continue
        
            elif seat == 'L':
                if (TASK == 1 and get_direct_neighbors(r,c) == 0) or \
                        (TASK == 2 and get_visible_neighbors(r,c) == 0):
                    next_grid[r][c] = '#'
                    changes += 1

            elif seat == '#':
                if (TASK == 1 and get_direct_neighbors(r,c) >= 4) or \
                        (TASK == 2 and get_visible_neighbors(r,c) >= 5):
                    next_grid[r][c] = 'L'
                    changes += 1

    grid = [r[:] for r in next_grid]

occupied_seats = 0
for r in grid:
    for c in r:
        if c == '#':
            occupied_seats += 1

print "task_{}: {}".format(TASK, occupied_seats)
