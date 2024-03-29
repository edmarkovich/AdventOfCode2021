from cmath import sqrt
import itertools
import math

file1 = open('day19.txt', 'r')
Lines = file1.readlines()

class Beacon:
    def __init__(self, coords):
        self.coords = coords
    
    def dist_vector(self, beacon):
        out = ( beacon.coords[0] - self.coords[0], 
                 beacon.coords[1] - self.coords[1],
                 beacon.coords[2] - self.coords[2])
        return out

    def clone_rotated(self,rot):
        axis = rot[0]
        sign = rot[1]
        out = ( self.coords[axis[0]] * sign[0], 
                 self.coords[axis[1]] * sign[1],
                 self.coords[axis[2]] * sign[2])
        return Beacon(out)

    def move(self, offset):
        x = (
            self.coords[0] - offset[0],
            self.coords[1] - offset[1],
            self.coords[2] - offset[2])
        self.coords = x
        return self

class Scanner:
    def __init__(self):
        self.beacons = [] #set()

    def add(self, beacon_line):
        b = beacon_line.split(",")
        b = map(lambda x: int(x), b)
        b = list(b)

        b = Beacon(b)
        self.beacons.append(b)
    
    def done(self):
        pass

    def get_rotated_beacons(self, rotation):
        return list(map(lambda x: x.clone_rotated(rotation), self.beacons))

    def clone_rotated(self,rotation):
        out = Scanner()
        out.beacons = self.get_rotated_beacons(rotation)
        return out


    def get_distance_vectors_for_beacon(self, beacon_id):
        out = []
        b1 = self.beacons[beacon_id]
        l = len(self.beacons)
        for i in range(0, l):
            if i == beacon_id: continue                    
            b2 = self.beacons[i]
            out.append(b1.dist_vector(b2))
        return out                            

    def normalize(self, rotation, offset):
        x = self.get_rotated_beacons(rotation)
        x = list(map(lambda a: a.move(offset), x))
        self.beacons = x        

def getAllRotations():
    if getAllRotations.cache == None:
        getAllRotations.cache=[]
        axis  = list(itertools.permutations([0,1,2]))
        signs = list(itertools.product([-1, 1], repeat=3))

        for a in axis:
            for s in signs:
                getAllRotations.cache.append((a,s))
    return getAllRotations.cache
getAllRotations.cache = None

def two_scanners_overlap(s1, s2_in):
    for r in getAllRotations():                    
        s2 = s2_in.clone_rotated(r)
        for x in range(0,len(s1.beacons)):
            s1_distances = s1.get_distance_vectors_for_beacon(x)
            s1_distances = set(s1_distances)
            for y in range(0, len(s2.beacons)):
                s2_distances = s2.get_distance_vectors_for_beacon(y)
                s2_distances = set(s2_distances)
                inter = s1_distances.intersection(s2_distances)
                if len(inter)>=11:
                    offset = s1.beacons[x].dist_vector(s2.beacons[y])
                    return (r, offset)
    return None

offsets=[(0,0,0)]
def translate_if_overlap(scanners, i, j):
    out = two_scanners_overlap(scanners[i], scanners[j])
    if out:
        rotation = out[0]
        offset   = out[1]
        print("Overlap between ",i,j, rotation, offset)
        offsets.append(offset)
        scanners[j].normalize(rotation, offset)
        return True
    return None


def find_overlapped_scanners(scanners):
        normalized = [0]
        processed  = []
        l = len(scanners)
        while True:
            change = False
            to_add=[]
            for i in normalized:                
                for j in range(0, l):
                    if i==j or (i,j) in processed or (j,i) in processed:
                        continue 
                    processed.append((i,j))
                    if translate_if_overlap(scanners,i,j):
                        to_add.append(j)   
                        change = True             
            if not change: 
                return normalized
            normalized += to_add

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
overlapped_ones = find_overlapped_scanners(scanners)


final = set()
for i in overlapped_ones:
    s = scanners[i]
    c = list(map( lambda x: (x.coords[0], x.coords[1], x.coords[2]), s.beacons))
    c = set(c)
    final.update(c)
print(len(final))

max_dist=0
l = len(offsets)
for i in range(0, l-1):
    for j in range (i, l):
        q = abs(offsets[i][0]-offsets[j][0])
        q += abs(offsets[i][1]-offsets[j][1])
        q += abs(offsets[i][2]-offsets[j][2])
        max_dist = max(max_dist,q)
print (max_dist)