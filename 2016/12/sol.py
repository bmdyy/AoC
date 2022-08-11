#!/usr/bin/python

instructions = [x.rstrip() for x in open("input","r")]
registers = {'a':0,'b':0,'c':0,'d':0}
eip = 0

while eip < len(instructions):
    c_instr = instructions[eip].split(" ")

    if c_instr[0] == "cpy":
        if c_instr[1].isdigit():
            registers[c_instr[2]] = int(c_instr[1])
        else:
            registers[c_instr[2]] = registers[c_instr[1]]

    elif c_instr[0] == "inc":
        registers[c_instr[1]] += 1
    
    elif c_instr[0] == "dec":
        registers[c_instr[1]] -= 1
    
    elif c_instr[0] == "jnz":
        if c_instr[1].isdigit():
            if int(c_instr[1]) != 0:
                eip += int(c_instr[2])
                continue

        elif registers[c_instr[1]] != 0:
            eip += int(c_instr[2])
            continue

    eip += 1
print(registers["a"])
