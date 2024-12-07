#!/usr/bin/python

# Advent of Code 2024, Day 7
# William Moody (@bmdyy)
# 07.12.2024

import itertools

with open("input.txt", "r") as f:
    eq = []
    for li in f.readlines():
        tk = li.strip().split(": ")
        eq.append((int(tk[0]), [int(n) for n in tk[1].split(" ")]))

def is_solvable(value, numbers, part):
    for ops in itertools.product(["+", "*", "|"] if part == 2 else ["+", "*"], repeat=len(numbers) - 1):
        tmp_value = numbers[0]
        for i in range(1, len(numbers)):
            if ops[i - 1] == "+":
                tmp_value = tmp_value + numbers[i]
            elif ops[i - 1] == "*":
                tmp_value = tmp_value * numbers[i]
            elif ops[i - 1] == "|":
                tmp_value = int(str(tmp_value) + str(numbers[i]))
        if tmp_value == value:
            return True
    return False

total_1 = 0
total_2 = 0
for value, numbers in eq:
   if is_solvable(value, numbers, part=1):
       total_1 += value
   if is_solvable(value, numbers, part=2):
       total_2 += value

print("Part 1:", total_1)
print("Part 2:", total_2)