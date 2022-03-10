import math
import itertools
import sys
import cProfile

file1 = open('day19.txt', 'r')
Lines = file1.readlines()

class Scanner:
    def __init__(self, beacons):
        self.beacons     = beacons
        self.distances   = None
        self.computeDistances()

    def distance(self, a, b):        
        x = (a[0]-b[0]) ** 2
        y = (a[1]-b[1]) ** 2
        z = (a[2]-b[2]) ** 2
        return int(math.sqrt(x+y+z)) #TODO: may need more precision

    def computeDistances(self):
        if self.distances != None: return self.distances

        self.distances = {}

        for i in range(0, len(self.beacons)):
            if i not in self.distances.keys(): self.distances[i]={}            

            for j in range (i+1, len(self.beacons)):
                if j not in self.distances.keys(): self.distances[j]={}

                self.distances[i][j] = self.distance(self.beacons[i], self.beacons[j])
                self.distances[j][i] = self.distances[i][j]
        
        return self.distances

    def countOverlap(self, otherSensor):
        x = self.computeDistances()        
        for beacon in x.keys():
            dists = x[beacon].values()
            matchedBeacon = otherSensor.findOverlap(dists)  
            if matchedBeacon != None:
                print(self.beacons[beacon], " -> ", matchedBeacon)

        return False
            
    def findOverlap(self, otherDistances):
        myDs = self.computeDistances()
        for myB in myDs.keys():
            overlap = set(myDs[myB].values()).intersection(set(otherDistances))
            if len(overlap) >= 11:
                return self.beacons[myB]
        return None




def loadScanners(Lines):
    scanners = []
    beacons = []
    for l in Lines:
        l = l.strip()

        if l.startswith("---"):
            beacons = []
            continue

        if l == "":
            if len(beacons) == 0: break
            s = Scanner(beacons)
            scanners.append(s)
            beacons=[]
            continue

        b = l.split(",")
        b = list(map(lambda x: int(x), b))
        beacons.append(b)
    
    return scanners

scans = loadScanners(Lines)

for i in range(0, len(scans)):
    for j in range(i+1, len(scans)):
        print(i,j)
        x = scans[i].countOverlap(scans[j])
        
        
