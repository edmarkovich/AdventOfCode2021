from operator import add


file1 = open('day12.txt', 'r')
Lines = file1.readlines()

paths = {}
def addPath(path):
    if path[0] not in paths.keys(): paths[path[0]] = []
    if path[1] not in paths.keys(): paths[path[1]] = []

    paths[path[0]].append(path[1])

    if path[0] != "start" and path[1] != "end":
        paths[path[1]].append(path[0])

def readFile():
    for line in Lines:
        path = line.strip().split("-")
        addPath(path)

def small(x):
    if x == None: return True
    return x[0] >= 'a' and x[0] <= 'z' and x not in ["start","end"]

def generatePaths(x,seen, doubled):

    if x == "end": 
        if doubled == None: return 1
        elif doubled == ' ': return 1
        return 0
    if x in seen:
        if x == doubled:
            doubled=' '
        else:
            return 0
    
    if small(x):
        seen = seen + [x]

    out = 0
    for n in paths[x]:
        out += generatePaths(n, seen, doubled)

    return out

readFile()
out = 0

for d in [None]+list(paths.keys()):

    if not small(d): continue
    out += generatePaths("start",[], d)
    print(d, out)