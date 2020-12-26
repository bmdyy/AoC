#!/usr/bin/python

in_ = "784235916"

cups = [int(x) for x in in_]

def disp_cups(curr):
    print "cups\t",
    for c in cups:
        if c == curr:
            print "("+str(c)+")",
        else:
            print str(c),
    print ""

current_cup = cups[0]
for move in range(100):
    print "-- move",(move+1),"--"

    # display cups
    disp_cups(current_cup)

    # pick up cups + display
    pickup = []
    for _ in range(3):
        pickup.append(cups.pop((cups.index(current_cup)+1)%len(cups)))
    print "pickup\t", " ".join([str(x) for x in pickup])

    # calc destination
    dest = current_cup - 1
    while dest in pickup or dest == 0:
        dest -= 1
        if dest <= 0:
            dest = max(cups)
    print "dest\t", dest

    # calculate index of destination cup
    j = cups.index(dest)

    # move the cups
    for p in pickup[::-1]:
        cups.insert(j+1, p)

    # update current cup
    current_cup = cups[(cups.index(current_cup) + 1) % len(cups)]

    print ""

print "-- final --"
disp_cups(current_cup)
