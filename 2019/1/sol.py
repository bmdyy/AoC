#!/usr/bin/python

modules = open("input", "r")

total = 0
for module in modules:
    total += int(module) // 3 - 2

print total
