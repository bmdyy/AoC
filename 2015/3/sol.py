#!/usr/bin/python
import sys

# handle args
if len(sys.argv) != 2:
    exit()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    exit()

f = open("input","r")
instr = f.readline().rstrip()
f.close()

x = [0,0]
y = [0,0]
turn = 0 # 0 = santa, 1 = robo
visited = [(x[0],y[0])]
for move in instr:
    if move == ">":
        x[turn] += 1
    elif move == "<":
        x[turn] -= 1
    elif move == "^":
        y[turn] += 1   
    elif move == "v":
        y[turn] -= 1

    for i in range(2):
        if (x[i],y[i]) not in visited:
            visited.append((x[i],y[i]))

    if TASK == 2:
        turn = 1 - turn

print len(visited)
