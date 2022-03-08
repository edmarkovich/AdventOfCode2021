import sys
from functools import reduce
import operator

file1 = open('day16.txt', 'r')
Lines = file1.readlines()

input= bin(int(Lines[0].strip(),16))[2:].zfill(4*len(Lines[0]))


def parseLiteral(stream):
    out = ""
    for i in range(0, len(stream)):
        out += stream[(i*5)+1:(i*5)+5]
        if stream[i*5]=="0":break
    lit = int(out,2)
    return (stream[(i*5)+5:], lit)

def parseOperator(op, stream):
    typ = stream[0]
    stream = stream[1:]
    subPackets = []
    if typ == "0":
        target = int(stream[0:15],2)
        stream = stream[15:]
        target = len(stream) - target
        while len(stream) > target:
            (stream, out) = parsePacket(stream)
            subPackets.append(out)
    else:
        target = int(stream[0:11],2)
        stream = stream[11:]
        for i in range(0, target):
            (stream, out) = parsePacket(stream)
            subPackets.append(out)

    out = None
    if   op == 0: out = sum(subPackets)
    elif op == 1: out = reduce(operator.mul, subPackets,1)
    elif op == 2: out = min(subPackets)
    elif op == 3: out = max(subPackets)
    elif op == 5: out = 1 if subPackets[0]>subPackets[1] else 0
    elif op == 6: out = 1 if subPackets[0]<subPackets[1] else 0
    elif op == 7: out = 1 if subPackets[0]==subPackets[1] else 0
    
    
    return (stream, out)

def parsePacket(stream):
    ver = int(stream[:3],2)
    stream = stream[3:]

    operator = int(stream[:3],2)
    stream = stream[3:]


    (stream, out) = parseLiteral(stream) if operator == 4 else parseOperator(operator, stream)

    return (stream, out)



(stream, out) = parsePacket(input)
print(out)
