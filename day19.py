import math
import itertools
file1 = open('day19.txt', 'r')
Lines = file1.readlines()

class Scanner:
    def __init__(self, beacons):
        self.beacons  = beacons
        self.scores   = None
        self.scoreMap = None

    def distance(self, a, b):
        print("Distance: ", a)
        x = (a[0]-b[0]) ** 2
        y = (a[1]-b[1]) ** 2
        z = (a[2]-b[2]) ** 2
        return math.sqrt(x+y+z)

    def scorePoints(self, subset):
        dist = []
        for a in subset:
            for b in subset:
                d = self.distance(a,b)
                if d != 0:
                    dist.append[d]
        return sorted(dist)

    def getCandidateScores(self):
        if self.scores != None:
            return self.scores

        self.scores = set()
        self.scoreMap = {}
        for poolSize in range(12, len(self.beacons)):
            comb  = itertools.combinations(self.beacons, poolSize)
            score = self.scorePoints(comb) 
            self.scores.add(score)
            self.scoreMap[score] = comb
        
        return self.scores


def loadScanners(Lines):
    scanners = []
    beacons = []
    for l in Lines:
        l = l.strip()

        if l.startswith("---"):
            beacons = []
            continue

        if l == "":
            print("Adding:", beacons)
            s = Scanner(beacons)
            scanners.append(s)
            continue

        b = l.split(",")
        b = list(map(lambda x: int(x), b))
        beacons.append(b)
    
    return scanners

scans = loadScanners(Lines)

for s in scans:
    print(s.getCandidateScores())
