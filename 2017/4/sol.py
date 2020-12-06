#!/usr/bin/python
import sys
import itertools

# handle args
if len(sys.argv) != 2:
    exit()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    exit()

def anagrams(word):
    return ["".join(perm) for perm in itertools.permutations(word)]        

def is_valid(password):
    tk = password.split(" ")
    for i in range(len(tk)):
        if TASK == 1:
            if tk[i] in tk[i+1:]:
                return False

        elif TASK == 2:
            for a in anagrams(tk[i]):
                if a in tk[i+1:]:
                    return False
    return True

print is_valid("abcde fghij")
print is_valid("abcde xyz ecdab")
print is_valid("a ab abc abd abf abj")
print is_valid("iiii oiii ooii oooi oooo")
print is_valid("oiii ioii iioi iiio")

print anagrams("abc")

passwords = [p for p in open("input", "r")]
valid = 0
for password in passwords:
    if is_valid(password.rstrip()):
        valid += 1
print valid
