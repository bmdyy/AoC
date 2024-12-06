#!/usr/bin/python

# Advent of Code 2024, Day 5
# William Moody (@bmdyy)
# 06.12.2024

with open("input.txt", "r") as f:
    rules, updates = f.read().split("\n\n")

rule_map = {}
for rule in rules.split("\n"):
    x, y = [int(n) for n in rule.split("|")]
    if not x in rule_map:
        rule_map[x] = [y]
    else:
        rule_map[x].append(y)

invalid_updates = []

mid_total = 0
for update in updates.split("\n"):
    is_valid_update = True

    update = [int(n) for n in update.split(",")]

    n = 1
    while is_valid_update and (n < len(update)):
        if update[n] in rule_map:
            for m in range(n):
                if update[m] in rule_map[update[n]]:
                    is_valid_update = False
        n += 1

    if is_valid_update:
        mid = update[int((len(update)-1)/2)]
        mid_total += mid
    else:
        invalid_updates.append(update)

print("Part 1:", mid_total)

def fix_update(u, i):
    if i < 0:
        return u

    #print("Index:", i, "Value:", u[i])

    if u[i] in rule_map:
        #print("- Rules:", rule_map[u[i]])
        for j in range(i):
            if u[j] in rule_map[u[i]]:
                #print("- - RULE_BREAK:",u[j],"at index (j)",j,"came before",u[i],"at index (i)",i)
                u2 = u[:j] + [u[i],u[j]] + u[j+1:i] + u[i+1:]
                #print(u2)
                return fix_update(u2, len(u2)-1)

    return fix_update(u, i-1)

mid_total = 0

for inv_update in invalid_updates:
    fixed_update = fix_update(inv_update, len(inv_update)-1)
    mid = fixed_update[int((len(fixed_update)-1)/2)]
    mid_total += mid

print("Part 2:", mid_total)