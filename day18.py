import json
import sys
file1 = open('day18.txt', 'r')
Lines = file1.readlines()


def readNumber(line):
    return(json.loads(line.strip()))

def explode(number):
    brackets = 0
    for i in range(0, len(number)):
        if number[i] == "[": brackets += 1
        if number[i] == "]": brackets -= 1

        if brackets == 5:
            for j in range(i+1, len(number)):
                if number[j] == "]":
                    target = number[i:j+1].replace("[","").replace("]","")
                    target = list(map(lambda x:int(x), target.split(",")))
                    out = number[0:i] + "0" + number[j+1:]

                    for k in range(i-1, 0, -1):
                        if out[k].isdigit():
                            t = int(out[k]) + target[0]
                            n = str(t) if t <10 else chr(ord("A")+t-10)
                            out = out[:k] + n + out[k+1:]

                            break

                    for k in range(i+1, len(out)):
                        if out[k].isdigit():
                            t = int(out[k]) + target[1]
                            n = str(t) if t <10 else chr(ord("A")+t-10)
                            out = out[:k] + n + out[k+1:]

                            break

                    return(out)

                    
def test():
    assert explode("[[[[[9,8],1],2],3],4]") == "[[[[0,9],2],3],4]"
    assert explode("[7,[6,[5,[4,[3,2]]]]]") == "[7,[6,[5,[7,0]]]]"
    assert explode("[[6,[5,[4,[3,2]]]],1]") == "[[6,[5,[7,0]]],3]"
    assert explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]") == "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"
    assert explode("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]") == "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"
test()

