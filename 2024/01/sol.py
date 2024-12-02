#!/usr/bin/python

# Advent of Code 2024, Day 1
# William Moody (@bmdyy)
# 02.12.2024

l1 = [] # Left list
l2 = [] # Right list

count_map = {} # The number of time a certain number appears in L2

with open("input.txt","r") as f:
    for line in f.readlines():
        n1, n2 = [int(n) for n in line.strip().split("   ")] 
        
        l1.append(n1)
        l2.append(n2)
        
        if n2 not in count_map:
            count_map[n2] = 1
        else:
            count_map[n2] += 1

# Sort both lists lowest to highest
l1.sort()
l2.sort()

# Calculate the total distance between the pairs
total_distance = sum([abs(l1[i] - l2[i]) for i in range(len(l1))])
print("Part 1:", total_distance)

# Calculate the similarity score
similarity_score = sum([l1[i] * (count_map[l1[i]] if l1[i] in count_map else 0) for i in range(len(l1))])
print("Part 2:", similarity_score)