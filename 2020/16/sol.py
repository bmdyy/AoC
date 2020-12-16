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

# determine which possible 
# orders there are
possible = []
for ticket in valid_tickets:
    order = [None] * len(ticket)
    for i in range(len(ticket)):
        for field_name in ranges:
            if (ticket[i] in ranges[field_name][0] or \
                    ticket[i] in ranges[field_name][1]) and \
                    field_name not in order:
                        order[i] = field_name
    if order not in possible:
        possible.append(order)

# check all tickets against all 
# possible orders until we find
# one which suits all
for order in possible:
    suitsAll = True
    for ticket in valid_tickets:
        for i in range(len(ticket)):
            if ticket[i] not in ranges[order[i]][0] and \
                    ticket[i] not in ranges[order[i]][1]:
                suitsAll = False

    # we have an order which works for all tickets
    if True:
        prod = 1
        for i in range(len(my_ticket)):
            if "departure" in order[i]:
                prod *= my_ticket[i]
        print prod
