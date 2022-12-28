#!/usr/bin/python3

# William Moody
# 28.12.2022

# Part One
ranges = [(pair[0].split("-"), pair[1].split("-")) for pair in [line.split(",") for line in open("input.txt", "r").read().split("\n")]]

total = 0
for r in ranges:
    if (r[0][0] <= r[1][0] and r[0][1] >= r[1][1]) or (r[1][0] <= r[0][0] and r[1][1] >= r[0][1]):
        total += 1
print(total)