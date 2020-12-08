#!/usr/bin/python
def run_program(instructions, task):
    acc = 0
    eip = 0

    while True:
        c_instr = instructions[eip]
    
        print 'eip=',eip, 'acc=',acc, 'c_instr=',c_instr

        # check if we were here before
        if (task == 1 and c_instr[1] > 0) or \
                (task == 2 and eip > len(instructions)):
            return acc
        c_instr[1] += 1
        
        op = c_instr[0][0]
        arg = int(c_instr[0][1])
        if op == "acc":
            acc += arg

        elif op == "jmp":
            eip += arg
            continue
        
        elif op == "nop":
            pass

        eip += 1

instructions = [[line.rstrip().split(" "), 0] for line in open("input", "r")]

print "task_1:",run_program(instructions[:], 1)

# we need to test all nop/jmps to be switched and then see if it exits
l_nr = 0
while l_nr < len(instructions):
    copy = [[line.rstrip().split(" "), 0] for line in open("input", "r")]

    if copy[l_nr][0][0] == "jmp":
        copy[l_nr][0][0] = "nop"
        #print l_nr,copy
        print "task2",run_program(copy, 1)

    elif copy[l_nr][0][0] == "nop":
        copy[l_nr][0][0] = "jmp"
        #print l_nr, copy
        print "task2",run_program(copy, 1)

    l_nr += 1
