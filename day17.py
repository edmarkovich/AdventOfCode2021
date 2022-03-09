file1 = open('day17.txt', 'r')
Lines = file1.readlines()

def getTgt(line):
    line = line.strip()
    line = line.split(': ')[1]
    line = line.split(", ")
    x = line[0].split("x=")[1].split("..")
    y = line[1].split("y=")[1].split("..")
    return(int(x[0]),int(x[1]),int(y[0]),int(y[1]))

(x1,x2,y1,y2) = getTgt(Lines[0])

def getViableXsteps(x1,x2):
    out = {}
    for i in range (0, x2+1): #initial speed
        speed = i
        travel = 0
        for j in range(1, x2+1): # number of steps
            travel += speed
            if travel >= x1 and travel <= x2:
                if j not in out.keys():
                    out[j]=set()
                out[j].add(i)          
            if speed >0:
                speed -= 1

    return (out)

def getBestY(y1,y2, xsteps):
    out = set()
    max_steps = max(xsteps.keys())
    for y in range(-100, 10000):
        speed = y
        travel = 0
        for s in range (1,max_steps+1):          
            travel += speed
            speed -= 1
            if travel >= y1 and travel <= y2 and s in xsteps.keys():
                out.update(list(map(lambda x: (x,y), xsteps[s])))
                
    return len(out)

xs = getViableXsteps(x1,x2)
y = getBestY(y1,y2,xs)
print(y)


