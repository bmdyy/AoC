#!/usr/bin/python
f = open("input", "r")
mem = [int(i) for i in f.readline().rstrip().split(",")]

# restore 1202
mem[1] = 12
mem[2] = 2

# run program
ptr = 0
while True:
    instr = mem[ptr]    

    if instr == 1:
        # add
        val_1 = mem[mem[ptr+1]]
        val_2 = mem[mem[ptr+2]]
        mem[mem[ptr+3]] = val_1 + val_2
        ptr += 4

    elif instr == 2:
        # mult
        val_1 = mem[mem[ptr+1]]
        val_2 = mem[mem[ptr+2]]
        mem[mem[ptr+3]] = val_1 * val_2
        ptr += 4

    elif instr == 99:
        # end
        print "Program halted"
        print "mem[0] = {}".format(mem[0])
        exit()
    else:
        print "ERROR! Invalid instruction: {}".format(instr)
        exit()
