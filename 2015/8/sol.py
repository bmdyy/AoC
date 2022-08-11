#!/usr/bin/python
import re

def escape(s):
    # remove quotes
    s = s[1:-1]
    # \\ -- \
    s = re.sub(r"\\\\", r"\\", s)
    # \" -- "
    s = re.sub(r'\\"', '"', s)
    # \x00 -- ascii byte
    s = re.sub(r'\\x[0-9a-f]{2}', '$', s) # placeholder $
    return s

def encode(s):
    # encode slashes
    s = re.sub(r'\\', r'\\\\', s)
    # encode quotes
    s = re.sub(r'"', r'\\"', s)

    # add quotes
    s = '"' + s + '"'
    return s

with open("input", "r") as f:
    code_length = 0
    string_length = 0
    enc_length = 0

    for line in f:
        # get rid of newlines [important!]
        line = line.rstrip()
        # count length of line for code_length
        esc = escape(line)
        # encode the string
        enc = encode(line)
        # add counts to the total
        code_length += len(line)
        string_length += len(esc)
        enc_length += len(enc)

    print "task_1:",code_length-string_length
    print "task_2:",enc_length-code_length

