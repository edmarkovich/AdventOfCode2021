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
    
    def dist(self, beacon):
        a = (self.coords[0] - beacon.coords[0]) ** 2
        b = (self.coords[1] - beacon.coords[1]) ** 2
        c = (self.coords[2] - beacon.coords[2]) ** 2
        r = (a+b+c) ** 0.5
        r = int(r)
        return(r)

class Scanner:
    def __init__(self):
        self.beacons = [] #set()
        self.distances = {}

    def add(self, beacon_line):
        b = Beacon(beacon_line)
        self.beacons.append(b)
        

    def done(self):
        l = len(self.beacons)
        for i in range(0, l-1):
            for j in range(i+1, l):
                self.distances[(i,j)] = self.beacons[i].dist(self.beacons[j])
        print(self.distances)



    

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


