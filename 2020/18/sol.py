#!/usr/bin/python
import re 

def _eval(expr):
    tk = expr.split(" ")
    t = int(tk[0])
    i = 1
    for i in range(len(tk)):
        if tk[i] == '+':
            t += int(tk[i+1])
            i += 1
        elif tk[i] == '*':
            t *= int(tk[i+1])
            i += 1
    return t

reg_abm = r"[0-9]+ \+ [0-9]+"
def _eval_abm(expr):
    s = re.search(reg_abm, expr)
    if s:
        g = s.group()
        r = eval(g)
        new_expr = expr.replace(g, str(r))
        return _eval_abm(new_expr)
    else:
        return eval(expr)

reg = r"\(([0-9]+ [\*|\+] )+[0-9]+\)"
def calc(expr, TASK):
    s = re.search(reg, expr)
    if s:
        g = s.group()
        r = calc(g[1:-1], TASK)
        new_expr = expr.replace(g, str(r))
        return calc(new_expr, TASK)
    else:
        if TASK == 1:
            return _eval(expr)
        else:
            return _eval_abm(expr)

for TASK in range(1,3):
    s = 0
    with open("input", "r") as f:
        for line in f:
            s += calc(line.rstrip(), TASK)
    print "task_{}: {}".format(TASK, s)
