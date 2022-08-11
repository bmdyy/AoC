#!/usr/bin/python

# wrapping paper
def wp(l,w,h):
    s = min([l*w, w*h, h*l])
    return 2*l*w + 2*w*h + 2*h*l + s

# ribbon
def ri(l,w,h):
    p = [l+l+w+w, w+w+h+h, h+h+l+l]
    b = l*w*h
    return min(p) + b

total_wp = 0
total_ri = 0
with open("input", "r") as f:
    for dim in f:
        dim = [int(i) for i in dim.split("x")]
        total_wp += wp(dim[0], dim[1], dim[2])
        total_ri += ri(dim[0], dim[1], dim[2])

print "task_1:",total_wp
print "task_2:",total_ri
