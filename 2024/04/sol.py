#!/usr/bin/python

# Advent of Code 2024, Day 4
# William Moody (@bmdyy)
# 06.12.2024

with open("input.txt", "r") as f:
    inp = [list(line.strip()) for line in f.readlines()]

rows = len(inp)
cols = len(inp[0])

count = 0

# N-S and S-N
for r in range(rows-3):
    for c in range(cols):
        if inp[r][c] == 'X' and inp[r+1][c] == 'M' and inp[r+2][c] == 'A' and inp[r+3][c] == 'S':
            count += 1
        elif inp[r][c] == 'S' and inp[r+1][c] == 'A' and inp[r+2][c] == 'M' and inp[r+3][c] == 'X':
            count += 1

# W-E and E-W
for r in range(rows):
    for c in range(cols-3):
        if inp[r][c] == 'X' and inp[r][c+1] == 'M' and inp[r][c+2] == 'A' and inp[r][c+3] == 'S':
            count += 1
        elif inp[r][c] == 'S' and inp[r][c+1] == 'A' and inp[r][c+2] == 'M' and inp[r][c+3] == 'X':
            count += 1

# NW-SE and SE-NW
for r in range(rows-3):
    for c in range(cols-3):
        if inp[r][c] == 'X' and inp[r+1][c+1] == 'M' and inp[r+2][c+2] == 'A' and inp[r+3][c+3] == 'S':
            count += 1
        elif inp[r][c] == 'S' and inp[r+1][c+1] == 'A' and inp[r+2][c+2] == 'M' and inp[r+3][c+3] == 'X':
            count += 1

# SW-NE and NE-SW
for r in range(3,rows):
    for c in range(cols-3):
        if inp[r][c] == 'X' and inp[r-1][c+1] == 'M' and inp[r-2][c+2] == 'A' and inp[r-3][c+3] == 'S':
            count += 1
        elif inp[r][c] == 'S' and inp[r-1][c+1] == 'A' and inp[r-2][c+2] == 'M' and inp[r-3][c+3] == 'X':
            count += 1

print("Part 1:",count)

# Visualization array
debug = []
for r in range(rows):
   debug.append([])
   for c in range(cols):
       debug[r].append(".")

# Reset the count for part two
count = 0

#  1     2     3     4
# M.S | S.S | S.M | M.M
# .A. | .A. | .A. | .A.
# M.S | M.M | S.M | S.S
for r in range(rows-2):
    for c in range(cols-2):
        if (inp[r][c] == 'M' and inp[r][c+2] == 'S' and inp[r+1][c+1] == 'A' and inp[r+2][c] == 'M' and inp[r+2][c+2] == 'S') or \
        (inp[r][c] == 'S' and inp[r][c+2] == 'S' and inp[r+1][c+1] == 'A' and inp[r+2][c] == 'M' and inp[r+2][c+2] == 'M') or \
        (inp[r][c] == 'S' and inp[r][c+2] == 'M' and inp[r+1][c+1] == 'A' and inp[r+2][c] == 'S' and inp[r+2][c+2] == 'M') or \
        (inp[r][c] == 'M' and inp[r][c+2] == 'M' and inp[r+1][c+1] == 'A' and inp[r+2][c] == 'S' and inp[r+2][c+2] == 'S'):
            count += 1

print("Part 2:",count)