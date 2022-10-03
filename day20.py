from cmath import sqrt
import itertools
import math

file1 = open('day20.txt', 'r')
Lines = file1.readlines()

class Beacon:
    def __init__(self, beacon_line):
        b = beacon_line.split(",")
        b = map(lambda x: int(x), b)
        b = list(b)
        self.coords = b
    
    def get_dist(self, beacon):
        a = (self.coords[0] - beacon.coords[0]) ** 2
        b = (self.coords[1] - beacon.coords[1]) ** 2
        c = (self.coords[2] - beacon.coords[2]) ** 2
        return (a+b+c) ** 0.5

class Scanner:
    def __init__(self):
        self.beacons = set()

    def add(self, beacon_line):
        b = Beacon(beacon_line)
        self.beacons.add(b)


    def done(self):
        pass      


    

scanners = []
scanner = None
for l in Lines:
    if l.startswith("---"):
        if scanner is not None:
            scanner.done()
        scanner = Scanner()
        scanners.append(scanner)
        continue
    if len(l.strip()) == 0:
        continue
    else:
        scanner.add(l.strip())
scanner.done()


