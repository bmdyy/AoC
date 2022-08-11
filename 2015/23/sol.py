#!/usr/bin/python
import sys

def usage():
    print "usage: %s <task>"
    print "where task is 1 or 2"
    exit()

# handle task arg
if len(sys.argv) != 2:
    usage()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    usage()

# parse the file
f = open("input", "r")
cmds = [cmd.rstrip().split(" ") for cmd in f]
f.close()

# calculate relative address
# given an offset and address
def rel_addr(addr, offset):
    val = int(offset[1:])
    if offset[0] == "+":
        addr += val
    else:
        addr -= val
    return addr

# simulate program
r = {'a':0 if TASK==1 else 1,
     'b':0} # registers
ip = 0 # instruction pointers
mii = len(cmds) # max instruction index

print "Lines: %d" % mii
print "Calls:\n"

while ip < mii:
    cmd = cmds[ip] # get current cmd

    print "%.2d> %s\t%d\t%d" % (ip," ".join(cmd),r['a'],r['b'])

    # hlf r
    # -- half register
    if cmd[0] == "hlf":
        r[cmd[1]] /= 2

    # tpl r
    # -- triple register
    elif cmd[0] == "tpl":
        r[cmd[1]] *= 3

    # inc r
    # -- increment register
    elif cmd[0] == "inc":
        r[cmd[1]] += 1

    # jmp offset
    # -- rel. jump to addr
    elif cmd[0] == "jmp":
        ip = rel_addr(ip, cmd[1])
        continue

    # jie r, offset
    # -- rel. jump if even
    elif cmd[0] == "jie":
        if r[cmd[1][:-1]] % 2 == 0:
            ip = rel_addr(ip, cmd[2])
            continue

    # jio r, offset
    # -- rel. jump if one
    elif cmd[0] == "jio":
        if r[cmd[1][:-1]] == 1:
            ip = rel_addr(ip, cmd[2])
            continue

    # unknown command
    else:
        print "ERROR @ ip={}: unknown command {}".format(ip, cmd)
        exit()
    
    # increase instr. pointer,
    # if there was no jumping
    ip = ip + 1

# print registers
print "\nRegisters:"
for r_ in r:
    print "%s: %d" % (r_, r[r_])
