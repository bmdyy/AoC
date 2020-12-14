#!/usr/bin/python
import itertools

def mask(m,i,t):
    b = bin(i)
    b_str = str(b)[2:]
    
    b_ = ""
    for i in range(1,len(m)+1):
        if m[-i] == '1' or m[-i] == '0':
            if t == 2 and m[-i] == '0' and i <= len(b_str):
                b_ = b_str[-i] + b_
            else:
                b_ = m[-i] + b_
        
        elif m[-i] == 'X':
            if t == 1 and i <= len(b_str):
                b_ = b_str[-i] + b_

            elif t == 1 and i > len(b_str):
                b_ = "0" + b_

            else:
                b_ = "X" + b_

    if t == 1:
        b_ = "0b" + b_
        b_ = int(b_, 2)

    return b_ 

def setc(s, i, c):
    s_ = s[:i] + c
    if i < -1:
        s_ = s_ + s[i+1:]
    return s_

def bin_len_n(n):
    h = 2 ** n
    r = []
    for i in range(h): # 2^n - 1
        s = str(bin(i))[2:]
        while len(s) < n:
            s = "0" + s
        r.append(s)
    return r

for TASK in range(1,3):
    m = None
    mem = {}
    with open("input", "r") as f:
        for line in f:
            cmd,val = line.rstrip().split(" = ")

            if cmd == "mask":
                m = val

            else:
                addr = cmd[4:-1]
                val = int(val)

                if TASK == 1:
                    mem[addr] = mask(m,val,1)

                elif TASK == 2:
                    m_ = mask(m,int(addr),2) 
                    x_ = []
                    for i in range(1,len(m_)+1):
                        if m_[-i] == 'X':
                            x_.append(-i)
                    x_l = len(x_)

                    blist = bin_len_n(x_l)
                    for i in range(len(blist)):
                        b_ = blist[i]
                        m__ = m_
                        for j in range(x_l):
                            m__ = setc(m__,x_[j],b_[j])
                        
                        addr = int("0b" + m__, 2)
                        mem[addr] = val
    total = 0
    for addr in mem:
        total += mem[addr]
    print "task_{}: {}".format(TASK, total)
