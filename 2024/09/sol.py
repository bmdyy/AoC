#!/usr/bin/python

# Advent of Code 2024, Day 9
# William Moody (@bmdyy)
# 09.12.2024

with open("input.txt","r") as f:
    diskmap = [int(n) for n in f.read().strip()]

size = sum(diskmap)

disk = [None] * size
free = []
ctr = 0
file_id = 0

for i in range(len(diskmap)):
    if i % 2 == 0: # File
        for j in range(diskmap[i]):
            disk[ctr] = file_id
            ctr += 1
        file_id += 1
    else: # Free space
        for j in range(diskmap[i]):
            free.append(ctr)
            ctr += 1

def print_info():
    for x in disk:
        print(str(x) if x != None else ".",end='')
    print() # print(" | Free:", free)

print_info()

i = size - 1
for _ in range(len(free)):
    if disk[i] != None:
        disk[free.pop(0)] = disk[i]
        disk[i] = None
    i -= 1
    print_info()

def checksum():
    ret = 0
    for i in range(size):
        if disk[i] == None:
            continue
        ret += i * disk[i]
    return ret

print("Part 1:",checksum())