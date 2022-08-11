#!/usr/bin/python
import sys
from colorama import Fore, Back, Style

def usage():
    print "{}{} TASK [-d]".format(Fore.RED, sys.argv[0])
    print "Where TASK is 1 or 2"
    print "Where -d is optional, to draw the grid"
    exit()

if len(sys.argv) != 2 and len(sys.argv) != 3:
    usage()

TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    usage()

DRAW_GRID = False
if len(sys.argv) == 3:
    if sys.argv[2] == '-d':
        DRAW_GRID = True

f = open("input", "r")

TREE = '#'
TREE_COLOR = Back.GREEN + Fore.GREEN
EMPTY = '.'
EMPTY_COLOR = Back.BLUE
TOBOGGAN = 'O'
TOBOGGAN_HIT = 'X'
TOBOGGAN_COLOR = Back.RED + Fore.RED

grid = []
for line in f:
    row = []
    for column in line.rstrip():
        row.append(column)
    grid.append(row)

slopes = []
if TASK == 1:
    slopes = [[3,1]]
else:
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
res = []

max_x = len(grid[0])
max_y = len(grid)

for slope in slopes:
    x = 0 # top left
    y = 0

    d_x = slope[0]
    d_y = slope[1]

    trees_hit = 0

    while y < max_y:
        if grid[y][x] == TREE:
            trees_hit = trees_hit + 1
    
        if DRAW_GRID:
            if grid[y][x] == TREE:
                grid[y][x] = TOBOGGAN_HIT
            else:
                grid[y][x] = TOBOGGAN

        x = (x + d_x) % max_x
        y += d_y

    if DRAW_GRID:
        for row in grid:
            r = " "
            for c in row:
                if c == EMPTY:
                    r += EMPTY_COLOR
                elif c == TREE:
                    r += TREE_COLOR
                else:
                    r += TOBOGGAN_COLOR

                r += c + Style.RESET_ALL
            print(r)
        print ""

    print "{}{}/{} -- {}".format(Fore.GREEN, d_x, d_y, trees_hit)
    if TASK == 2:
        res.append(trees_hit)

if TASK == 2:
    total = 1
    for run in res:
        total *= run
    print "\n{}{}".format(Fore.GREEN, total)
