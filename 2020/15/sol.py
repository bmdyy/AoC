#!/usr/bin/python
for TASK in range(1,3):
    starting_numbers = [int(x) for x in "0,1,4,13,15,12,16".split(",")]
    last_number = 0

    spoken = {} # n : [last_last_spoken, last_spoken]

    turn = 1
    last_turn = 2020 if TASK == 1 else 30000000

    # starting numbers
    for number in starting_numbers:
        spoken[number] = [turn, turn]

        last_number = number
        turn += 1

    # game loop
    out = -1
    while turn <= last_turn:
        # was spoken before
        if last_number in spoken:
            # first time being spoken
            if spoken[last_number][0] == spoken[last_number][1]:
                out = 0

            # not the first time
            else:
                out = spoken[last_number][1] - spoken[last_number][0]

        # print "T"+str(turn)+": "+str(last_number)+" => "+str(out)

        if out in spoken:
            spoken[out][0] = spoken[out][1]
            spoken[out][1] = turn
        else:
            spoken[out] = [turn, turn]

        last_number = out
        turn += 1

    print "task_{}: {}".format(TASK, out)
