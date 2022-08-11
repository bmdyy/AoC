#!/usr/bin/python
import sys

# handle args
if len(sys.argv) != 2:
    exit()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    exit()

# init our light array
light_array = []
for i in range(1000):
    r = []
    for j in range(1000):
        r.append(0)
    light_array.append(r)

# loop through the instructions
instructions = [line.rstrip() for line in open("input","r")]
for i in instructions:
    cmd = i[0:7]
    split = i.split(" ")
    r0,c0 = split[-3].split(",")
    r1,c1 = split[-1].split(",")

    for r in range(int(r0), int(r1)+1):
        for c in range(int(c0), int(c1)+1):
            val = light_array[r][c]
            new_val = 0
            if cmd == "toggle ":
                new_val = (1-val) if TASK == 1 else (val+2)
            elif cmd == "turn of":
                new_val = 0 if TASK == 1 else ((val-1) if val > 0 else 0)
            elif cmd == "turn on":
                new_val = 1 if TASK == 1 else (val+1)
            light_array[r][c] = new_val

# count total lights that are on
total_val = 0
for i in range(1000):
    for j in range(1000):
        if light_array[i][j] > 0:
            total_val += light_array[i][j]
print "task_%d: %d" % (TASK, total_val)
