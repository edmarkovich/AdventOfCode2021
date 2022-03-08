file1 = open('day14.txt', 'r')
Lines = file1.readlines()


template = ""
map = {}

for l in Lines:
    l = l.strip()
    if template == "" : 
        template = l
        continue
    if l == "":
        continue
    l = l.split(" -> ")
    map[l[0]] = l[1]


def getMap(a,b):
    k=a+b
    if k not in map.keys(): return ""
    return map[k]

def compute(template):    
    out = template[0]
    for i in range (0, len(template)-1):
        k = getMap(template[i], template[i+1])
        out += k + template[i+1]
    return out

def score(x, levels):
    s=x
    for i in range(0,levels):
        s=compute(s)
    print("Got it: ",x,s)


cache={}
def run(template):
    if template in cache:
        return cache[template]


    mid = int(len(template)/2)
    if mid<3: 
        return compute(template)

    a = template[0:mid]    
    b = template[mid:]
    out = run(a) + getMap(a[-1], b[0]) + run(b)
    cache[template]=out
    return out


score("VF",10)

import sys
sys.exit()


for i in range(0,10):
    cache={}
    template = run(template)


m1 = len(template)
m2 = 0

for i in template:
    l = template.count(i)
    m1 = min(m1, l)
    m2 = max(m2, l)

print (m2-m1)
