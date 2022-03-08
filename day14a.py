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

def resolve(a,b):
    k=a+b
    if k not in map.keys(): return [a+b]
    k=map[k]
    return [a+k,k+b]

cache ={}

def compute(template, levels):    
    global cache

    if levels==0:         
        return {template[0]: 1}

    if levels not in cache.keys():
        cache[levels]={}

    out = {}
    for i in range (0, len(template)-1):
        k = resolve(template[i], template[i+1])
        for p in k:
            if p not in cache[levels].keys(): 
                cache[levels][p] = compute(p, levels-1)
            for x in cache[levels][p]:
                if x not in out.keys():
                    out[x]=0
                out[x] += cache[levels][p][x]
    return out



print(template)
out = compute(template,40)
out[template[-1]] += 1

m1 = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
m2 = 0

for i in out:
    l = out[i]
    m1 = min(m1, l)
    m2 = max(m2, l)

print (m2-m1)
