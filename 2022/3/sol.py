#!/usr/bin/python3

# William Moody
# 28.12.2022

# Part One
print(sum([(ord(x[0]) - (96 if ord(x[0])>=97 else 38)) for x in [list(set(r[:len(r)//2]) & set(r[len(r)//2:])) for r in open("input.txt","r").read().split("\n")]]))

# Part Two
lines = open("input.txt","r").read().split("\n")
print(sum([[(ord(x[0]) - (96 if ord(x[0])>=97 else 38)) for x in list(set(lines[i]) & set(lines[i+1]) & set(lines[i+2]))][0] for i in range(0, len(lines), 3)]))