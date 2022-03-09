import json
import math
import sys
file1 = open('day18.txt', 'r')
Lines = file1.readlines()


def readNumber(line):
    return(json.loads(line.strip()))

def int2str(t):
    return str(t) if t <10 else chr(ord("a")+t-10)

def str2int(t):
    if t.isdigit(): return int(t)
    return 10 + ord(t) - ord("a")



def explode(number):
    #print(number)
    brackets = 0
    for i in range(0, len(number)):
        if number[i] == "[": brackets += 1
        if number[i] == "]": brackets -= 1

        if brackets == 5:
            for j in range(i+1, len(number)):
                if number[j] == "]":
                    #print(number[i:j+1])
                    target = number[i:j+1].replace("[","").replace("]","")
                    target = list(map(lambda x:str2int(x), target.split(",")))
                    out = number[0:i] + "0" + number[j+1:]

                    for k in range(i-1, 0, -1):
                        if out[k] not in "[],": #.isdigit() or out[k].isalpha():
                            t = str2int(out[k]) + target[0]
                            n = int2str(t)
                            out = out[:k] + n + out[k+1:]

                            break

                    for k in range(i+1, len(out)):
                        if out[k] not in "[],": #.isdigit() or out[k].isalpha():
                            
                            t = str2int(out[k]) + target[1]
                            n = int2str(t)

                            if out[k] == "W":
                                print(out[k], target[1],t,n)

                            out = out[:k] + n + out[k+1:]

                            break

                    return(out)
    return None

def split(number):
    for i in range (0, len(number)):
        if number[i] not in "[],": #.isalpha():
            n = str2int(number[i])
            if n<10: continue

            a = math.floor(n/2)
            a = int2str(a)
            b = math.ceil(n/2)
            b = int2str(b)
            return number[:i]+"["+a+","+b+"]"+number[i+1:]
    return None

def add(a,b):
    num = "["+a+","+b+"]"
    while True:
        changed = False
        while True:
            x = explode(num)
            if x == None: break
            changed = True
            num = x
        
        
        x = split(num)
        if x == None:
            if not changed: return num
        else:
            num =x

def addList(l):
    out = l[0]
    for i in range(1, len(l)):
        out = add(out,l[i])
    return out
                    
def test():
    assert explode("[[[[[9,8],1],2],3],4]") == "[[[[0,9],2],3],4]"
    assert explode("[7,[6,[5,[4,[3,2]]]]]") == "[7,[6,[5,[7,0]]]]"
    assert explode("[[6,[5,[4,[3,2]]]],1]") == "[[6,[5,[7,0]]],3]"
    assert explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]") == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
    assert explode("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]") == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"

    assert explode("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]") == "[[[[0,7],4],[7,[[8,4],9]]],[1,1]]"
    #assert explode("[[[[0,7],4],[7,[[8,4],9]]],[1,1]]") == "[[[[0,7],4],[F,[0,D]]],[1,1]]"
    #assert split("[[[[0,7],4],[F,[0,D]]],[1,1]]") == "[[[[0,7],4],[[7,8],[0,D]]],[1,1]]"
    #assert split("[[[[0,7],4],[[7,8],[0,D]]],[1,1]]") == "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"
    assert explode("[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]") == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

    assert add("[[[[4,3],4],4],[7,[[8,4],9]]]","[1,1]") == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"


    assert addList(["[1,1]","[2,2]","[3,3]","[4,4]"]) == "[[[[1,1],[2,2]],[3,3]],[4,4]]"

    l = [
        "[1,1]",
        "[2,2]",
        "[3,3]",
        "[4,4]",
        "[5,5]",
        "[6,6]"]
    assert addList(l)== "[[[[5,0],[7,4]],[5,5]],[6,6]]"

    l = ["[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
    "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
    "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
    "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
    "[7,[5,[[3,8],[1,4]]]]",
    "[[2,[2,2]],[8,[8,1]]]",
    "[2,9]",
    "[1,[[[9,3],9],[[9,0],[0,7]]]]",
    "[[[5,[7,4]],7],1]",
    "[[[[4,2],2],6],[8,7]]"]
    assert addList(l) == "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"

test()
  