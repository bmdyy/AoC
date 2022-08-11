#!/usr/bin/python
rules = {}
test_cases = []

def is_valid(case):
    return False 

with open("test", "r") as f:
    # parse the rules
    line = None
    while True:
        line = f.readline().rstrip().replace('"', '')
        if line == "":
            break
        tk = line.split(": ")
        rules[int(tk[0])] = [[int(y) if y.isdigit() else y for y \
                in x.split(" ")] for x in tk[1].split(" | ")]
    
    # parse the test cases
    line = None
    while True:
        line = f.readline().rstrip()
        if line == "":
            break
        test_cases.append(line)
