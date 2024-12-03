#!/usr/bin/python

# Advent of Code 2024, Day 3
# William Moody (@bmdyy)
# 03.12.2024

import re
import math

with open("input.txt", "r") as f:
    memory = "".join(f.readlines()).strip()

parse_memory = lambda m : sum([math.prod([int(n) for n in instr[4:-1].split(",")]) for instr in re.findall(r"mul\(\d+,\d+\)", m)])

print("Part 1:", parse_memory(memory))
print("Part 2:", sum([parse_memory(section.split("don't()")[0]) for section in memory.split("do()")]))