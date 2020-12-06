#!/usr/bin/python
import sys

# handle args
if len(sys.argv) != 2:
    exit()
TASK = int(sys.argv[1])
if TASK < 1 or TASK > 2:
    exit()

# weird data struct
# very bad
# very inefficient
# dont use
class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.parent = None
        self.children = []

    def __str__(self):
        if self.has_parent():
            # has a parent
            return "%s:%d [parent--%s]" % (self.name, self.get_weight(), self.parent)
        else:
            # is a parent
            return "%s:%d" % (self.name, self.get_weight())

    def set_parent(self, parent):
        self.parent = parent
        return self

    def has_parent(self):
        return self.parent != None

    def add_child(self, c):
        self.children.append(c)

    def has_children(self):
        return len(self.children) > 0

    def get_weight(self):
        if self.has_children():
            w = self.weight
            for c in self.children:
                w += c.get_weight()
            return w
        else:
            # leaf node
            return self.weight

# gets a node from the list
# by node name
def get_node(nodes, name):
    for n in nodes:
        if n.name == name:
            return n

# list of nodes
nodes = []

# loop through the lines and store in array
f = open("input", "r")
lines = []
for line in f:
    lines.append(line)
f.close()


# first add all nodes without 
# considering who the parent is
for line in lines:
    towers = line.strip().split(" -> ")
    parent = towers[0].replace("(","").replace(")","").split(" ")
    parent[1] = int(parent[1]) # parse weight value

    n = Node(parent[0], parent[1])
    nodes.append(n)

# next check for parent relationships
# now that all nodes are in the list
# yes. this is very inefficient
for line in lines:
    towers = line.strip().split(" -> ")
    parent = towers[0].replace("(","").replace(")","").split(" ")
    parent[1] = int(parent[1]) # parse weight value

    # parent node
    p = get_node(nodes, parent[0])

    # is a parent node
    if len(towers) > 1:
        children = towers[1].split(", ")
        for child in children:
            c = get_node(nodes, child).set_parent(p)
            p.add_child(c)
          
# print root node
for n in nodes:
    # only if root
    if not n.has_parent():
        root = n

if TASK == 1:
    print root.name

def which_is_unbalanced(children):
    # returns weight, index

    last = children[0].get_weight()
    last_c = children[0]
    for i in range(1, len(children)):
        c_w = children[i].get_weight()
        if c_w != last:
            return last_c
        last = c_w
    return 'balanced' # balanced

if TASK == 2:
    un = which_is_unbalanced(root.children)
    last_un = un
    while un != 'balanced':
        last_un = un
        un = which_is_unbalanced(un.children)
    
    # node which must change weight is last_un
    a = last_un.get_weight()
    for c in last_un.parent.children:
        if c != last_un:
            b = c.get_weight() # weight it should have
            break

    print last_un.weight - abs(b-a)
