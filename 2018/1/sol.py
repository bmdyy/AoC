#!/usr/bin/python
f = open("input", "r")

freq = 0
for freq_change in f:
    sign = freq_change[0]
    val = int(freq_change[1:])

    if sign == '+':
        freq += val
    elif sign == '-':
        freq -= val

print freq
f.close()
