#!/usr/bin/python

class Bag:
    def __init__(self, num, col):
        self.col = col
        self.num = num
        self.holds = []

    def _holds(self, bag):
        self.holds.append(bag)
   
    def get_child(self, bag):
        for b in self.holds:
            if b.col == bag.col:
                return b 
        for b in self.holds:
            r = b.get_child(bag)
            if r != None:
                return r
        return None

    def weight(self):
        total = 0
        for child in self.holds:
            if child.num != 0:
                total += child.num * (1 + child.weight())
        return total

    def __str__(self):
        if len(self.holds)>0:
            s = []
            for h in self.holds:
                s.append(h.__str__())
            s=" + ".join(s)
            return "%d %s [HOLDS %s]" % (self.num, self.col, s)
            #return "%d+%d*(%s)" % (self.num, self.num, s)
        else:
            return "%d %s" % (self.num, self.col)
            #return "%d" % self.num

lines = [line.rstrip() for line in open("input", "r")]
holds_our_targets = []
we_want = ["shiny gold"]
shiny_holds = []
root = Bag(1, "shiny gold")
last_len = 0
while last_len != len(we_want):
    last_len = len(we_want)
    for line in lines:
        tk = line.split(" contain ")
        outer = tk[0][:-5]
        inner = tk[1].split(", ")
        
        for i in inner:
            i2 = i.replace("no other","0")
            i2 = i2.split(" ")
            num = int(i2[0])
            col = " ".join(i2[1:3]) # other, bags if num = 0

            if outer == "shiny gold" and [num,col] not in shiny_holds:
                shiny_holds.append([num,col])
                root._holds(Bag(num, col))

            for o in shiny_holds:
                if outer == o[1] and [num,col] not in shiny_holds:
                    shiny_holds.append([num,col])
                    root.get_child(Bag(o[0],o[1]))._holds(Bag(num,col))

            for w in we_want:
                if w == col and outer not in holds_our_targets:
                    holds_our_targets.append(outer)
            
    for h in holds_our_targets:
        if h not in we_want:
            we_want.append(h)

print "task_1:",len(holds_our_targets)
print "task_2: GAVE UP ON THIS" 
