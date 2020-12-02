#!/usr/bin/python
import sys

def usage():
    print "usage: {} TASK".format(sys.argv[0])
    print "TASK = 1 or 2"
    exit()

if len(sys.argv) != 2:
    usage()

TASK = 0
if int(sys.argv[1]) >= 1 and int(sys.argv[1]) <= 2:
    TASK = int(sys.argv[1])
else:
    usage()

f = open('input','r')

num_valid = 0
for line in f:
    tokens = line.rstrip().split(': ')
    policy = tokens[0].split(' ')
    
    indicies = policy[0].split('-')
    letter = policy[1]
    password = tokens[1]

    if TASK == 1:
        num_c = 0
        for c in password:
            if c == letter:
                num_c = num_c + 1
        
        if int(indicies[0]) <= num_c and num_c <= int(indicies[1]):
            num_valid = num_valid + 1
    
    else:
        num_pos = 0
        for i in range(len(password)):
            if password[i] == letter and str(i + 1) in indicies:
                num_pos = num_pos + 1
        
        if num_pos == 1:
            num_valid = num_valid + 1

f.close()
print num_valid
