#!/usr/bin/python

# Advent of Code 2024, Day 2
# William Moody (@bmdyy)
# 02.12.2024

inp = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        inp.append([int(n) for n in line.strip().split(" ")])

def is_safe(rep):
    # All increasing OR All decreasing
    # Any two adjacent differ by 1-3
    last = rep[0]
    is_asc = rep[1] > rep[0]
    for i in range(1, len(rep)):
        diff = abs(rep[i] - last)
        if diff < 1 or diff > 3:
            return False
        if is_asc and rep[i] < last:
            return False
        last = rep[i]
    return True

num_safe = 0
for report in inp:
    num_safe += 1 if is_safe(report) else 0

print(num_safe)