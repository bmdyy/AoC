#!/usr/bin/python

# Advent of Code 2024, Day 2
# William Moody (@bmdyy)
# 03.12.2024

inp = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        inp.append([int(n) for n in line.strip().split(" ")])

def is_safe(rep):
    is_asc = rep[1] > rep[0]

    i = 1
    while i < len(rep):
        # All increasing OR All decreasing
        if is_asc and (rep[i] <= rep[i-1]):
            return False
        elif not is_asc and (rep[i] >= rep[i-1]):
            return False

        # Any two adjacent must differ by 1-3
        diff = abs(rep[i] - rep[i-1])
        if diff < 1 or diff > 3:
            return False

        i = i + 1

    return True

# This is definitely not the most efficient solution,
# however, it works.
def is_safe_ex(rep):
    # Check if the base report is safe
    if is_safe(rep):
        return True

    # Create a copy of the list without a single element and check if it is safe
    for i in range(len(rep)):
        rep_copy = rep.copy()
        rep_copy.pop(i)
        if is_safe(rep_copy):
            return True

num_safe = sum([1 if is_safe(r) else 0 for r in inp])
print("Part 1:", num_safe)

num_safe_with_dampener = sum([1 if is_safe_ex(r) else 0 for r in inp])
print("Part 2:", num_safe_with_dampener)