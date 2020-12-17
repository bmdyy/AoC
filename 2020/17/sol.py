#!/usr/bin/python
grid = []
PADDING = 10
ROUNDS = 6
VISUAL = False

def disp_grid():
    z_str = ""
    for z in range(len(grid)):
        z_str += "z="+str(z)+" "*(len(grid))+"\t"
    print z_str
    for y in range(len(grid[0])):
        z_str = ""
        for z in range(len(grid)):
            z_str += "".join(grid[z][y])
            z_str += "\t"
        print z_str

def check_neighbors(x,y,z):
    active = 0
    inactive = 0
    for z_ in range(z-1,z+2):
        for y_ in range(y-1,y+2):
            for x_ in range(x-1,x+2):
                if x_==x and y_==y and z_==z:
                    continue
                if (z_<0 or z_>=len(grid)) or \
                   (y_<0 or y_>=len(grid[0])) or \
                   (x_<0 or x_>=len(grid[0][0])):
                    continue
    
                if grid[z_][y_][x_] == '#':
                    active += 1
                else:
                    inactive += 1

    return active, inactive

with open("input","r") as f:
    plain = []
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
        grid.append([['.']*len(plain[0])]*len(plain[0]))
    grid.append(plain)
    for i in range(PADDING):
        grid.append([['.']*len(plain[0])]*len(plain[0]))

if VISUAL:
    disp_grid()

for r in range(ROUNDS):
    new_grid = [[[x for x in y] for y in z] for z in grid]
    if VISUAL:
        print "...{}/{}...".format(r+1,ROUNDS)
    # first cycle
    for z in range(len(grid)):
        for y in range(len(grid[z])):
            for x in range(len(grid[z][y])):
                ca = grid[z][y][x] == '#'
                a,i = check_neighbors(x,y,z)
                if ca and (a==2 or a==3):
                    pass

                elif ca and a!=2 and a!=3:
                    new_grid[z][y][x] = '.'

                elif not ca and a==3:
                    new_grid[z][y][x] = '#'

                elif not ca and a!=3:
                    pass

    grid = [[[x for x in y] for y in z] for z in new_grid]
    if VISUAL:
        disp_grid()

active = 0
for z in grid:
    for y in z:
        for x in y:
            if x == '#':
                active += 1
print "task_1:",active
