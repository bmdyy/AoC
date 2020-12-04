#!/usr/bin/python
f = open("input", "r")
freq_changes = [[l[0], int(l[1:])] for l in f]

freqs = []
freq = 0
dup_found = False
i = 0
max_i = len(freq_changes)
while not dup_found:
    if freq_changes[i][0] == '+':
        freq += freq_changes[i][1]
    else:
        freq -= freq_changes[i][1]

    if freq in freqs:
        print freq
        exit()

    freqs.append(freq)
    i = (i + 1) % max_i
