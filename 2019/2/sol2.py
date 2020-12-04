#!/usr/bin/python
output = 0
looking_for = 19690720

noun = 0
verb = 0

while verb <= 99:
    f = open("input", "r")
    mem = [int(i) for i in f.readline().rstrip().split(",")]
    f.close()

    # 0 - 99 inclusive
    mem[1] = noun # noun
    mem[2] = verb # verb
    
    print "noun: {}, verb: {}".format(noun, verb)

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
           output = mem[0]
           break
 
        else:
           print "ERROR! Invalid instruction: {}".format(instr)
           exit()

    if output == looking_for:
        print "FOUND IT!"
        print 100 * noun + verb
        exit()

    noun += 1
    if noun > 99:
        noun = 0
        verb += 1
