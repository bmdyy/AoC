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
                    #print(update[m],"came before",update[n],"!")
                    is_valid_update = False
        n += 1

    if is_valid_update:
        #print(update)
        mid = update[int((len(update)-1)/2)]
        mid_total += mid
    else:
        invalid_updates.append(update)

print("Part 1:", mid_total)

# TODO: