import sys

file1 = open('day16.txt', 'r')
Lines = file1.readlines()

input= bin(int(Lines[0].strip(),16))[2:].zfill(4*len(Lines[0]))


def parseLiteral(stream):
    out = ""
    for i in range(0, len(stream)):
        out += stream[(i*5)+1:(i*5)+5]
        if stream[i*5]=="0":break
    lit = int(out,2)
    #return (stream[(i*5)+5:], lit)
    return (stream[(i*5)+5:], 0) #no version for literars

def parseOperator(stream):
    typ = stream[0]
    stream = stream[1:]
    outVer = 0
    if typ == "0":
        target = int(stream[0:15],2)
        stream = stream[15:]
        target = len(stream) - target
        while len(stream) > target:
            (stream, out) = parsePacket(stream)
            outVer += out
    else:
        target = int(stream[0:11],2)
        stream = stream[11:]
        for i in range(0, target):
            (stream, out) = parsePacket(stream)
            outVer += out
    return (stream, outVer)

def parsePacket(stream):
    ver = int(stream[:3],2)
    stream = stream[3:]

    typ = int(stream[:3],2)
    stream = stream[3:]


    (stream, out) = parseLiteral(stream) if typ == 4 else parseOperator(stream)

    return (stream, ver+out)



(stream, out) = parsePacket(input)
print(out)
