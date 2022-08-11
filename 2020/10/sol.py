#!/usr/bin/python
from itertools import permutations

def load_file():
    a = [int(x.rstrip()) for x in open("input","r")]
    a.sort()
    return a

adapters = load_file()
built_in = max(adapters) + 3

adapters.append(built_in)
adapters.insert(0, 0) # wall

j1_differences = 0
j3_differences = 0

last_adapter = adapters[0]
cur = 1

before = 0

while cur < len(adapters):
    cur_adapter = adapters[cur]
    next_adapter = adapters[cur+1] if cur+1<len(adapters) else built_in

    before = cur_adapter - last_adapter

    if before == 1:
        j1_differences += 1
    elif before == 3:
        j3_differences += 1


    last_adapter = cur_adapter
    cur += 1

print "task_1:", j1_differences * j3_differences

adapters = [0] + load_file() + [built_in]
combos = [1] + [0] * (len(adapters) - 1)
# loop through adapters
for i in range(1, len(adapters)):
    total = 0
    # check the last 3 adapters, to see if they are within 
    # 3 joltages of the current one. If yes, then add their
    # permutations into the new total
    for j in range(1, 4):
        if i-j >= 0 and adapters[i] - adapters[i-j] <= 3:
            total += combos[i-j]
    combos[i] = total
print "task_2:", combos[-1]
