#!/usr/bin/python
import re
import sys

# IMPORTANT:
# 'input' must end with a newline,
# otherwise there is an off by one error

def usage():
    print "Usage: {} TASK".format(sys.argv[0])
    print "Where TASK is 1 or 2"
    exit()

# handle arguments
TASK = 1
if len(sys.argv) != 2:
    usage()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    usage()

class Passport:
    values = {'byr':'','iyr':'','eyr':'','hgt':'',
              'hcl':'','ecl':'','pid':'','cid':''}

    rules = {'byr':'^19[2-9][0-9]|200[0-2]$',
             'iyr':'^20(1[0-9]|20)$',
             'eyr':'^20(2[0-9]|30)$',
             'hgt':'(^1([5-8][0-9]|9[0-3])cm$)|(^(59|6[0-9]|7[0-6])in$)',
             'hcl':'^#[0-9a-f]{6}$',
             'ecl':'^amb|b(lu|rn)|gr(y|n)|hzl|oth$',
             'pid':'^[0-9]{9}$',
             'cid':''}

    def __init__(self):
        for k in self.values:
            self.values[k] = ''

    def set(self, key, val):
        # if input is invalid, leave field empty
        if TASK == 1 or (TASK == 2 and re.search(self.rules[key], val)):
            self.values[key] = val

    def validate(self):
        for k in self.values:
            if self.values[k] == '' and k != 'cid': # cid optional
                return False
        return True

# open file
f = open('input', 'r')
lines = [line.rstrip() for line in f]
f.close()

num_valid = 0
p = Passport()

# loop through the passports
for line in lines:
    if line == '':
        # end of passport, validate it
        if p.validate():
            num_valid += 1
        p = Passport()
        continue

    for tks in line.split(' '):
        tk = tks.split(':')
        p.set(tk[0], tk[1])

# output
print num_valid
