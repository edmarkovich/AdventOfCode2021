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
        self.relocated   = False

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

    def getOverlaps(self, otherSensor):
        x = self.computeDistances()   
        out =[]     
        for beacon in x.keys():
            dists = x[beacon].values()
            matchedBeacon = otherSensor.findOverlapByDistances(dists)  
            if matchedBeacon != None:
                out.append((self.beacons[beacon], matchedBeacon))                

        return out
            
    def findOverlapByDistances(self, otherDistances):
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

def getDistVect(a,b):
    return( a[0]-b[0], a[1]-b[1], a[2]-b[2] )

def getTranslator(colSeq, colSign):
    funcA = None
    if colSeq == 1: funcA = lambda x : (x[0], x[1], x[2])
    if colSeq == 2: funcA = lambda x : (x[0], x[2], x[1])
    if colSeq == 3: funcA = lambda x : (x[1], x[0], x[2])
    if colSeq == 4: funcA = lambda x : (x[1], x[2], x[0])
    if colSeq == 5: funcA = lambda x : (x[2], x[0], x[1])
    if colSeq == 6: funcA = lambda x : (x[2], x[1], x[0])

    if colSign == 1: funcB = lambda x : (x[0], x[1], x[2])
    if colSign == 2: funcB = lambda x : (-x[0], x[1], x[2])
    if colSign == 3: funcB = lambda x : (x[0], -x[1], x[2])
    if colSign == 4: funcB = lambda x : (x[0], x[1], -x[2])
    if colSign == 5: funcB = lambda x : (-x[0], -x[1], x[2])
    if colSign == 6: funcB = lambda x : (x[0], -x[1], -x[2])    
    if colSign == 7: funcB = lambda x : (-x[0], -x[1], -x[2]) 

    g = lambda x: funcB(funcA(x))
    return g

def findFindAxisFunction(overlappedBeacons):
    for a in range(1,6):
        for b in range (1, 8):
            axisFunction = getTranslator(a,b)

            test = list(map(lambda x: (x[0], axisFunction(x[1])), overlappedBeacons))
            test = list(filter(lambda x: getDistVect(x[0], x[1]), test))
            print("    :", test)
            if len(test) == len(overlappedBeacons):
                return axisFunction
    print("No Axis rotator?!")


def findMoveVector(overlappedBeacons):

    for i in range(0, len(overlappedBeacons)-1):
        x1 = getDistVect(overlappedBeacons[i][0], overlappedBeacons[i+1][0])
        x2 = getDistVect(overlappedBeacons[i][1], overlappedBeacons[i+1][1])
        if x1 == x2 : 
            offset = getDistVect(overlappedBeacons[i][1], overlappedBeacons[i][0])
            print("OOOOOH",overlappedBeacons[i][0], overlappedBeacons[i][1], offset)
            return offset
        print("WTF?!",x1,x2)
    print("ERROR?!")


def getScanPairsForMatching(scans):
    relocated = []
    todo      = []

    for s in scans:
        if s.relocated:  relocated.append(s)
        else:            todo.append(s)

    if todo == []: return None

    out = []
    for r in relocated:
        for t in todo:
            out.append( (r,t) )

    return out


scans = loadScanners(Lines)
scans[0].relocated = True

while True:
    pairs = getScanPairsForMatching(scans)
    if pairs == None: break

    for p in pairs:
        overlaps = p[0].getOverlaps(p[1])
        if overlaps == []: 
            continue

        print(overlaps[0])

        p[1].relocated = True
        axisFunction = findFindAxisFunction(overlaps)

        overlapWithRotation = list(map(lambda x: (x[0], axisFunction(x[1])), overlaps))
        print(overlapWithRotation[0])

        sys.exit()

        findMoveVector(overlapWithRotation)
        





        
