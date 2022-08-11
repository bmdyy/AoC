#!/usr/bin/python
with open("test", "r") as f:
    tile_num = f.readline().rstrip().split(" ")[1][:-1]
    print tile_num

