#!/usr/bin/python

ranges = {}
my_ticket = []
nearby_tickets = []

# parse the file
with open("input", "r") as f:
    while True:
        line = f.readline().rstrip()
        if line == "":
            break
        line = line.split(": ")
        key = line[0]
        line = line[1].split(" ")
        r1 = [int(n) for n in line[0].split("-")]
        r2 = [int(n) for n in line[2].split("-")]
        ranges[key] = [range(r1[0],r1[1]+1), range(r2[0],r2[1]+1)]
    
    f.readline() # your ticket:
    my_ticket = [int(n) for n in f.readline().rstrip().split(",")]

    f.readline() # empty line
    f.readline() # nearby tickets:
    line = f.readline()
    while line != "":
        nearby_tickets.append([int(n) for n in line.rstrip().split(",")])
        line = f.readline()

# loop through the tickets
# and find invalid fields
valid_tickets = []
error_rate = 0
for ticket in nearby_tickets:
    valid_ticket = True
    for field in ticket:
        valid = False
        for field_name in ranges:
            if field in ranges[field_name][0] or \
                    field in ranges[field_name][1]:
                valid = True
                break
        if not valid:
            error_rate += field
            valid_ticket = False
    if valid_ticket:
        valid_tickets.append(ticket)

print "task_1:", error_rate

# determine all possiblities for
# each field
possible = {}
# loop through all valid tickets
for ticket in valid_tickets:
    # loop through all fields of the ticket
    for i in range(len(ticket)):
        # check the field against all
        # possible ranges, to see which are
        # possibilites at this position
        for field_name in ranges:
            if ticket[i] in ranges[field_name][0] or \
                    ticket[i] in ranges[field_name][1]:
                if field_name in possible and \
                        i not in possible[field_name]:
                    possible[field_name].append(i)
                else:
                    possible[field_name] = [i]

# create a list of the fields
# we have left to allocate a position
# in the final order
fields_left = []
for field_name in ranges:
    fields_left.append(field_name)

# store the final order
order = [None] * len(fields_left)

for i in range(1, len(possible)):
    possible[i-1] = list(set(possible[i]) - set(possible[i-1]))

# loop until we ordered all field
# names in their respective positions
while len(fields_left) > 0:
    for field in fields_left:
        if len(possible[field]) == 1:
            i = possible[field][0]
            order[i] = field
            fields_left.remove(field)
            for p in possible:
                if i in possible[p]:
                    possible[p].remove(i)
            print order
            print fields_left
            print possible
