#!/usr/bin/python
def is_valid(n, preamble):
    for i in preamble:
        for j in preamble:
            if n == i + j:
                return True
    return False

def load_numbers():
    return [int(n) for n in open("input", "r")]

preamble_len = 25
numbers = load_numbers()
preamble = numbers[:preamble_len]
numbers = numbers[preamble_len:]

# find invalid number
invalid_num = 0
for n in numbers:
    if not is_valid(n, preamble):
        invalid_num = n
        break

    preamble.pop(0)
    preamble.append(n)

print "task_1:", invalid_num

# find contiguous set adding up to that number
numbers = load_numbers()
for i in range(len(numbers)):
    for j in range(len(numbers)-i):
        total = 0
        for k in range(i, j):
            total += numbers[k]
            if total > invalid_num:
                continue
        if total == invalid_num:
            min_in_r = min(numbers[i:j])
            max_in_r = max(numbers[i:j])
            print "task_2:",min_in_r + max_in_r
            exit()
