#!/usr/bin/python

with open("input", "r") as f:
    d = {}

    for line in f:
        line = line.rstrip()
        outer, inner = line.split(" contain ")
        outer = outer[:-5]

        for i in inner.replace("no", "0").split(", "):
            i = i.split(" ")
            num = i[0]
            col = " ".join(i[1:3])
            tmp = "x".join([num,col])

            if outer in d:
                d[outer].append(tmp)
            else:
                d[outer] = [tmp]

def can_contain(col):
    target_colors = [col]

    for i in range(5):
        for outer in d:        
            all_contents = d[outer]
            for contains in all_contents:
                color = contains.split("x")[1]
                if color in target_colors:
                    if outer not in target_colors:
                        target_colors.append(outer)
    return len(target_colors)-1 # " -1 to ignore shiny gold

def get_contents(col):
    total = 0

    dec = col.split('x')
    num = int(dec[0])
    col = dec[1]

    if col == "other bags.":
        return 0
    else:
        for child in d[col]:
            child_num = int(child.split("x")[0])
            total = total + child_num * (get_contents(child) + 1)

    return total

print "task_1:",can_contain("shiny gold")
print "task_2:",get_contents("1xshiny gold")
