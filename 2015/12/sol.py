#!/usr/bin/python
import json

def sum_numbers(js,ignore=None):
    # first convert js into a json object
    data = json.loads(js)
    total = 0
   
    # loop through the items (keys or values)
    # in the json object
    for d in data:
        # get data types of the element, as 
        # well as the element in which it is contained
        t = type(d)
        s = type(data)

        # if we get a number, just
        # add it to the total
        if t == int:
            total += d
        # if we get a dict or list, we call
        # sum_numbers recursively on the re-encoded
        # json string
        elif t == dict or t == list:
            total += sum_numbers(json.dumps(d), ignore)
        # if we are in a dict, and our data element
        # is a unicode string, it is the key for an element
        # and we need to check what type that element is.
        # if the child element is an int, we can add it to
        # the total, if it is a list or dict, we call
        # sum_numbers recursively again. otherwise just ignore
        elif s == dict and t == unicode:
            x = type(data[d])
            if x == int:
                total += data[d]
            # for task 2, we need to check if any
            # value in a dictionary is 'red', in which 
            # case we are to ignore all total counts from
            # this dictionary. I generalized it here to
            # ignore any value passed to the var ignore
            elif ignore != None and x == unicode and data[d] == ignore:
                return 0
            elif x == list or x == dict:
                total += sum_numbers(json.dumps(data[d]), ignore)
        # if a data element is none of those data types
        # we can safely ignore it
    
    return total

with open("input","r") as f:
    line = f.readline().rstrip()
   
    print "task_1:",sum_numbers(line)
    print "task_2:",sum_numbers(line,"red")
