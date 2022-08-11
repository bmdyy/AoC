#!/usr/bin/python

def get_groups(x):
    groups = []
    c_group = [-1,0]
    # loop through all characters in the
    # strings and generate the groups
    for i in range(len(x)):
        # create the first group, or we
        # are extending the current group
        if c_group == [-1,0] or \
                c_group[0] == x[i]:
            c_group[0] = x[i]
            c_group[1] += 1
        # group ended, so we add it to the
        # array and start a new one
        else:
            # we add a COPY of c_group to groups
            # the copy is created with slicing
            groups.append(c_group[:])
            c_group[0] = x[i]
            c_group[1] = 1
    # add the last group (since it 'doesn't end')
    groups.append(c_group)
    return groups

# the 'brains' of this is the grouping
# function I designed above. here we just
# concat the results of that function to a string
def look_and_say(x):
    y = ""
    groups = get_groups(x)
    for group in groups:
        y += str(group[1])
        y += group[0]
    return y

# simulate a look-and-say game
def simulate(p_input, p_rounds):
    for r in range(p_rounds):
        p_input = look_and_say(p_input)
    return p_input

# init puzzle config
puzzle_input = "3113322113"

# print output
print "task_1:",len(simulate(puzzle_input, 40))
print "task_2:",len(simulate(puzzle_input, 50))
