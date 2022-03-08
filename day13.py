file1 = open('day13.txt', 'r')
Lines = file1.readlines()

fold = False
dots= []
folds=[]
for line in map(lambda x: x.strip(), Lines):
    if line == "":
        print('----')
        fold=True
        continue
    if not fold:
        dots.append(list(map(lambda x: int(x), line.split(','))))
    else:
        t=line.split(' ')[2].split('=')
        t[1] = int(t[1])
        folds.append(t)


def doFold(axis, line):
    global dots
    out = []
    if axis=='y':
        for dot in dots:
            if dot[1]< line: 
                if dot not in out: out.append(dot)
                continue
            dot[1] = line - (dot[1]-line)

            if dot not in out: out.append(dot)
    if axis=='x':

        for dot in dots:
            if dot[0]< line: 

                if dot not in out: out.append(dot)
                continue
            
            x = line - (dot[0]-line)
            #print(dot[0],line,dot[0]-line,x)
            dot[0]=x
            if dot not in out: out.append(dot)            
    dots=out

for f in folds:
    doFold(f[0],f[1])
    print(":",len(dots))

x=0
y=0
for d in dots:
    x=max(x, d[0])
    y=max(y, d[1])

for j in range (0,y+1):
    line=""
    for i in range(0,x+1):
        if [i,j] in dots: line += "#" 
        else: line +=" "
    print(line)
