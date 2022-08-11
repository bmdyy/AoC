#!/usr/bin/python
from copy import deepcopy

def run_program(instructions):
    acc = 0
    eip = 0

    while eip < len(instructions):
        c_instr = instructions[eip]

        #print 'eip=',eip, 'acc=',acc, 'c_instr=',c_instr

        # check if we were here before
        if (c_instr[1] > 0):
            return (None,acc)
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
    return (True,acc) # task 2

def load_file():
    return [[line.rstrip().split(" "), 0] for line in open("input", "r")]

instructions = load_file()
print "task_1:",run_program(instructions)[1]

# we need to test all nop/jmps to be switched and then see if it exits
l_nr = 0
while l_nr < len(instructions):
    copy = load_file()
    if copy[l_nr][0][0] == "jmp" or copy[l_nr][0][0] == "nop":
        copy[l_nr][0][0] = "nop" if copy[l_nr][0][0] == "jmp" else "nop"
        ret = run_program(copy)
        if ret[0] == True:
            print "task_2:",ret[1]

    l_nr += 1
