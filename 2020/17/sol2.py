#!/usr/bin/python
grid = []
PADDING = 10
ROUNDS = 6

def check_neighbors(x,y,z,w):
    active = 0
    inactive = 0
    for w_ in range(w-1,w+2):
        for z_ in range(z-1,z+2):
            for y_ in range(y-1,y+2):
                for x_ in range(x-1,x+2):
                    if x_==x and y_==y and z_==z and w_==w:
                        continue
                    if (w_<0 or w_>=len(grid)) or \
                        (z_<0 or z_>=len(grid[w_])) or \
                        (y_<0 or y_>=len(grid[w_][z_])) or \
                        (x_<0 or x_>=len(grid[w_][z_][y_])):
                        continue
                    if grid[w_][z_][y_][x_] == '#':
                        active += 1
                    else:
                        inactive += 1

    return active, inactive

with open("input","r") as f:
    plain = []
    three = []
    for row in f:
        r = ['.']*PADDING
        for col in row.rstrip():
            r.append(col)
        for i in range(PADDING):
            r.append('.')
        plain.append(r)
    for i in range(PADDING):
        plain.insert(0,['.']*len(plain[0]))
        plain.append(['.']*len(plain[0]))
    for i in range(PADDING):
        three.append([['.']*len(plain[0])]*len(plain[0]))
    three.append(plain)
    for i in range(PADDING):
        three.append([['.']*len(plain[0])]*len(plain[0]))
   
    for i in range(PADDING+1):
        grid.append([[['.']*len(plain[0])]*len(plain[0])]*len(plain[0]))
    grid.append(three)
    for i in range(PADDING+1):
        grid.append([[['.']*len(plain[0])]*len(plain[0])]*len(plain[0]))

for r in range(ROUNDS):
    new_grid = [[[[x for x in y] for y in z] for z in w] for w in grid]
    print "...{}/{}...".format(r+1,ROUNDS)
    # first cycle
    for w in range(len(grid)):
        for z in range(len(grid[w])):
            for y in range(len(grid[w][z])):
                for x in range(len(grid[w][z][y])):
                    ca = grid[w][z][y][x] == '#'
                    a,i = check_neighbors(x,y,z,w)
                    if ca and (a==2 or a==3):
                        pass

                    elif ca and a!=2 and a!=3:
                        new_grid[w][z][y][x] = '.'

                    elif not ca and a==3:
                        new_grid[w][z][y][x] = '#'

                    elif not ca and a!=3:
                        pass

    grid = [[[[x for x in y] for y in z] for z in w] for w in new_grid]

active = 0
for w in grid:
    for z in w:
        for y in z:
            for x in y:
                if x == '#':
                    active += 1
print "task_2:",active
