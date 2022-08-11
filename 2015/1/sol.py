#!/usr/bin/python
f = open("input","r")
instr = f.readline().rstrip()
f.close()

floor = 0
entered_basement = False
for i in range(len(instr)):
    cmd = instr[i]
    floor = floor + (1 if cmd=="(" else -1)
    if floor == -1 and not entered_basement:
        entered_basement = True
        print "task_2:",(i+1)

print "task_1:",floor
