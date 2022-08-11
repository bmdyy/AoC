#!/usr/bin/python

# returns winning player's score
def combat(d1,d2):
    r_num = 1
    while d1 != [] and d2 != []:
        print "-- Round {} --".format(r_num)
        print "P1's deck:", ", ".join(d1)
        print "P2's deck:", ", ".join(d2)

        p1 = d1.pop(0)
        p2 = d2.pop(0)

        print "P1 plays:", p1
        print "P2 plays:", p2
       
        if int(p1) > int(p2):
            d1.append(p1)
            d1.append(p2)
            print "P1 wins the round!"

        elif int(p2) > int(p1):
            d2.append(p2)
            d2.append(p1)
            print "P2 wins the round!"

        else:
            print "Uh oh"

        print ""
        r_num += 1
    
    print "== Post-game results =="
    print "P1's deck:", ", ".join(d1)
    print "P2's deck:", ", ".join(d2)
    print ""

    dw = []
    if d1 == []:
        dw = d2[::-1]
    else:
        dw = d1[::-1]

    s = 0
    i = 1
    for card in dw:
        s += i*int(card)
        i += 1
    return s

deck_1 = []
deck_ = []
with open("input", "r") as f:
    # read the input file (decks)
    f.readline() # Player 1:
    line = None
    while line != "":
        line = f.readline().rstrip()
        deck_1.append(line)
    deck_1 = deck_1[:-1] # remove the ""
    f.readline() # Player 2:
    line = None
    while line != "":
        line = f.readline().rstrip()
        deck_2.append(line)
    deck_2 = deck_2[:-1]

t1 = combat(deck_1, deck_2)
print "task_1:",t1
