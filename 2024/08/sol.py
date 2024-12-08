#!/usr/bin/python

# Advent of Code 2024, Day 8
# William Moody (@bmdyy)
# 08.12.2024

import itertools

with open("input.txt", "r") as f:
    inp = [list(line.strip()) for line in f.readlines()]

# def print_board():
#     for r in range(len(inp)):
#         for c in range(len(inp[r])):
#             print(inp[r][c], end='')
#         print()

rows = len(inp)
cols = len(inp[0])

antennas = {}
for r in range(rows):
    for c in range(cols):
        if inp[r][c] != '.':
            if inp[r][c] not in antennas:
                antennas[inp[r][c]] = []
            antennas[inp[r][c]].append((r,c))

# --- Part 1
antinodes = []
for antenna_type in antennas:
    if len(antennas[antenna_type]) > 1:
        for antenna_pair in itertools.combinations(antennas[antenna_type], 2):
            distance = (antenna_pair[0][0] - antenna_pair[1][0], antenna_pair[0][1] - antenna_pair[1][1])
            antinode_1 = (antenna_pair[0][0] + distance[0], antenna_pair[0][1] + distance[1])
            antinode_2 = (antenna_pair[1][0] - distance[0], antenna_pair[1][1] - distance[1])
            
            if (antinode_1[0] >= 0 and antinode_1[0] < rows) and (antinode_1[1] >= 0 and antinode_1[1] < cols):
                antinodes.append((antinode_1[0], antinode_1[1]))

            if (antinode_2[0] >= 0 and antinode_2[0] < rows) and (antinode_2[1] >= 0 and antinode_2[1] < cols):
                antinodes.append((antinode_2[0], antinode_2[1]))

antinodes = list(dict.fromkeys(antinodes))
print("Part 1:", len(antinodes))

# --- Part 2
antinodes = []
print("Part 2:", len(antinodes))