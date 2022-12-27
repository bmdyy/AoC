#!/usr/bin/python3

# William Moody
# 27.12.2022

sums = [sum(int(n) for n in elf.split("\n")) for elf in open("input.txt","r").read().split("\n\n")]
sums.sort(reverse=True)

print("Solution 1:", sums[0])
print("Solution 2:", sums[0]+sums[1]+sums[2])