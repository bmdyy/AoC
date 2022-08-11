#!/usr/bin/python

modules = open("input", "r")

total = 0
for module in modules:
    fuel_required = int(module) // 3 - 2
    while fuel_required > 0:
        total += fuel_required
        fuel_required =  fuel_required // 3 - 2

print total
