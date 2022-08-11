#!/usr/bin/python
from math import log

mod = 20201227 # prime

# https://helloacm.com/compute-powermod-abn/
def powermod(a, b, n):
    r = 1
    while b > 0:
        if b & 1 == 1:
            r = r * a % n
        b /= 2
        a = a * a % n
    return r

def transform(subject, loop_size):
    return powermod(subject, loop_size, mod)

def determine_loop_size(public_key):
    val = 1
    loops = 1

    while True:
        val = (val * 7) % mod
        if val == public_key:
            return loops
        loops += 1

with open("input","r") as f:
    card_pub = int(f.readline().rstrip())
    door_pub = int(f.readline().rstrip())
    print "Card public:",card_pub
    print "Door public:",door_pub

card_loop_size = determine_loop_size(card_pub)
door_loop_size = determine_loop_size(door_pub)
print "Card loop size:", card_loop_size
print "Door loop size:", door_loop_size

priv = transform(card_pub, door_loop_size)
print "Private key:", priv
