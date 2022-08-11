#!/usr/bin/python

# each hex is defined by
# coordinates:
# x;y;z

# Cube coordinates, as defined here
# https://math.stackexchange.com/questions/2254655/hexagon-grid-coordinate-system

def get_coords(steps, relative):
    x = relative[0]
    y = relative[1]
    z = relative[2]
    i = 0
    while i < len(steps):
        if steps[i] == 'e': 
            x += 1
            y -= 1
        
        elif steps[i] == 'w':
            x -= 1
            y += 1

        elif steps[i:i+2] == 'se':
            y -= 1
            z += 1

        elif steps[i:i+2] == 'sw':
            x -= 1
            z += 1
        
        elif steps[i:i+2] == 'nw':
            y += 1
            z -= 1
        
        elif steps[i:i+2] == 'ne':
            x += 1
            z -= 1
    
        i += 1 if steps[i] in ['e', 'w'] else 2

    return "{};{};{}".format(x,y,z)

grid = {}

with open("test", "r") as f:
    for steps in f:
        coords = get_coords(steps, [0,0,0])

        if coords in grid:
            grid[coords] = 1 - grid[coords]
        else:
            grid[coords] = 1

def count_blacks():
    total = 0
    for x in grid:
        total += grid[x]
    return total

# part 1
print "task 1:", count_blacks()
print ""
