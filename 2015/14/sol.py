#!/usr/bin/python

class Reindeer():
    # create new instance
    def __init__(self, name, kms, duration, rest):
        self.name = name
        self.kms = kms
        self.duration = duration
        self.rest = rest

        self.distance = 0
        self.points = 0

        self.ticks = 0
        self.resting = False

    # simulate one second
    def tick(self):
        # if we are not resting, go forwards
        if not self.resting:
            self.distance += self.kms

        # increment ticks, of course
        self.ticks += 1

        # if we are not resting, and we used up all of our flying
        # duration, start resting
        if not self.resting and self.ticks == self.duration:
            self.resting = True
            self.ticks = 0

        # if we are resting and used up all rest ticks, we can
        # start flying again
        elif self.resting and self.ticks == self.rest:
            self.resting = False
            self.ticks = 0

    # to string
    def __str__(self):
        return '%4d ~ %4d ~ %s' % (self.distance, self.points, self.name)

class Race():
    def __init__(self, reindeers):
        self.reindeers = reindeers
        
    # simulate second for all reindeers
    def tick(self):
        for r in self.reindeers:
            r.tick()
        
        self.lb_distance().points += 1

    # leader by distance
    def lb_distance(self):
        leader = self.reindeers[0]
        for r in self.reindeers:
            if r.distance > leader.distance:
                leader = r
        return leader

    # leader by points
    def lb_points(self):
        leader = self.reindeers[0]
        for r in self.reindeers:
            if r.points > leader.points:
                leader = r
        return leader

race_length = 2503 # seconds
with open("input", "r") as f:
    # create all reindeer objects
    reindeers = []
    for line in f:
        tmp = line.rstrip().split(" ")
        reindeers.append(Reindeer(tmp[0], int(tmp[3]), \
                int(tmp[6]), int(tmp[13])))

    # create a race object
    race = Race(reindeers)

    # simulate the race for the given
    # number of seconds
    for t in range(race_length):
        race.tick()

    # TASK 1
    # print out the winning distance
    # TASK 2
    # print number of winning points
    print "Task_1:",race.lb_distance().distance
    print "Task_2:",race.lb_points().points
