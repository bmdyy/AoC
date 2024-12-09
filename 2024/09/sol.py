#!/usr/bin/python

# Advent of Code 2024, Day 9
# William Moody (@bmdyy)
# 09.12.2024

with open("input.txt","r") as f:
    diskmap = [int(n) for n in f.read().strip()]

############### PART 1 ###############

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
    print() #print(" | Free:", free)

#print_info()

i = size - 1
for _ in range(len(free)):
    if disk[i] != None:
        disk[free.pop(0)] = disk[i]
        disk[i] = None
    i -= 1
    #print_info()

def checksum():
    ret = 0
    for i in range(size):
        if disk[i] == None:
            continue
        ret += i * disk[i]
    return ret

print("Part 1:",checksum())

############### PART 2 ###############

files = []
free = []
ctr = 0
file_id = 0

for i in range(len(diskmap)):
    if i % 2 == 0: # File
        files.append([file_id, ctr, ctr + diskmap[i]])
        file_id += 1
        ctr += diskmap[i]
    else: # Free space
        free.append([ctr, ctr + diskmap[i]])
        ctr += diskmap[i]

c_file_id = files[-1][0] 
while c_file_id > files[0][0]:
    file_len = files[c_file_id][2] - files[c_file_id][1]

    for i in range(len(free)):
        if free[i][1] - free[i][0] >= file_len and free[i][0] < files[c_file_id][1]:
            files[c_file_id][1] = free[i][0]
            files[c_file_id][2] = free[i][0] + file_len
            free[i][0] += file_len
            if free[i][0] == free[i][1]:
                free.pop(i)
            break

    c_file_id -= 1

disk = [None] * size
for f in files:
    for i in range(f[1], f[2]):
        disk[i] = f[0]

# print_info()

print("Part 2:", checksum())