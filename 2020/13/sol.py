#!/usr/bin/python

start_time = 0
lines = []
with open("input","r") as f:
    start_time = int(f.readline())
    lines = [x for x in f.readline().rstrip().split(",")]

# task 1
min_wait = 999999
min_line = - 1
for line in lines:
    if line == 'x':
        continue
    line = int(line)
    tmp = line - (start_time % line)
    if tmp < min_wait:
        min_wait = tmp
        min_line = line

print "task_1:",min_line * min_wait

# task 2
a = []
m = []
for i in range(len(lines)):
    if lines[i] == 'x':
        continue
    a.append(int(lines[i]) - i)
    m.append(int(lines[i]))

N = 1
for m_ in m:
    N *= m_

n = []
for m_ in m:
    n.append(N/m_)

u = []
for i in range(len(n)):
    u_ = 1
    while (n[i]*u_) % m[i] != 1:
        u_ += 1
    u.append(u_)

x = 0
for i in range(len(a)):
    x += a[i] * n[i] * u[i]

print "task_2:",x % N
