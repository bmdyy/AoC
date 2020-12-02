#!/usr/bin/python

f = open('input','r')

num_valid = 0
for line in f:
    tokens = line.rstrip().split(': ')
    policy = tokens[0].split(' ')
    
    positions = policy[0].split('-')
    letter = policy[1]
    password = tokens[1]

    num_pos = 0
    for i in range(len(password)):
        if password[i] == letter and str(i + 1) in positions:
            num_pos = num_pos + 1

    if num_pos == 1:
        num_valid = num_valid + 1

f.close()
print num_valid
