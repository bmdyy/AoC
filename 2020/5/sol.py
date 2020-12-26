#!/usr/bin/python
import sys

# handle arg
if len(sys.argv) != 2:
    exit()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    exit()

# the boarding pass is just 
# a binary number
def seat_id(bsp):
    r = 0
    for i in range(7):
        if bsp[i] == 'B':
            r += 2**(6-i)
    
    c = 0
    for i in range(3):
        if bsp[i+7] == 'R':
            c += 2**(2-i)

    return r * 8 + c # seat id

# parse the file
seats = [seat_id(i) for i in open("aoc_day5","r")]

if TASK == 1:
    print max(seats)
else:
    seats.sort()
    last_seat = seats[0]
    for i in range(1, len(seats)):
        if seats[i] - last_seat != 1:
            print last_seat + 1
        last_seat = seats[i]
