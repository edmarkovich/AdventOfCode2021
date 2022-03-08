import sys

file1 = open('day15.txt', 'r')
Lines = file1.readlines()

def endPos(grid):
    row = len(grid)
    col = len(grid[0])
    return (row-1,col-1)

def makeCosts():
    out = []
    dim = len(grid)

    for i in range(0, dim):
        x = []
        for j in range(0,dim):
            x.append(None)
        out.append(x)
    return out

def getNs(x,y):
    out = []
    (endx, endy) = endPos(grid)
    if x>0:     out.append( (x-1, y))
    if x<endx:  out.append( (x+1, y))
    if y>0:     out.append( (x, y-1))
    if y<endy:  out.append( (x, y+1))
    return out

grid = []
import sys
def makeGrid():
    global grid
    grid = list(map(lambda x: list(map(lambda y: int(y), x.strip())), Lines))

    dim = len(grid)


    for row in grid:
        out=[]
        for i in range(1,5):
            new = list(map(lambda x: x+i, row))
            new = list(map(lambda x: x-9 if x > 9 else x, new))
            out += new
        row += out  

    for t in range (1,5):
        for row in range (0,dim):
            new = list(map(lambda x: x+t, grid[row]))
            new = list(map(lambda x: x-9 if x > 9 else x, new))
            grid.append(new)


makeGrid()


costs = makeCosts()
    


def doRipple(dist):
    mod = False
    (endx, endy) = endPos(grid)
    if dist == 0:
        costs[endx][endx] = grid[endx][endy]
        return False
    
    points = []
    for i in range(endx-dist, endx+1):
        points.append( (i, endy-dist))
        points.append( (endy-dist, i))
    
    for (x,y) in points:
        ns = getNs(x,y)        
        c= 999999999999999999999999999999999999999999999999999999999999999999999
        for (xn,xy) in ns:
            cn = costs[xn][xy]
            if cn == None: continue
            c = min(c,cn)    
        if c == 999999999999999999999999999999999999999999999999999999999999999999999:
            continue
        c = grid[x][y] + c
        if c!= costs[x][y]: 
            mod = True
            costs[x][y] = c
    return mod
            
mod = 1

while mod:
    mod = 0
    for i in range(0, len(grid)):
        x = doRipple(i)
        if x: mod += 1
    print(mod)
    
print(costs[0][0]-grid[0][0])







