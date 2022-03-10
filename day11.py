file1 = open('day11.txt', 'r')
Lines = file1.readlines()

board = []
for line in Lines:
	line = line.strip()
	line = list(map(lambda x: int(x), line))
	board.append(line)

rows = len(board)
cols = len(board[0])

def addOne():
	out = list(map(lambda x: list(map(lambda y: y if y>0 else 0, x)), board))
	out = list(map(lambda x: list(map(lambda y: y +1, x)), out))
	return out

def getNs(i,j):
	out = []
	rs = [i]
	cs = [j]
	if i>0: rs.append(i-1)
	if i<rows-1: rs.append(i+1)
	if j>0: cs.append(j-1)
	if j<cols-1: cs.append(j+1)
	for x in rs:
		for y in cs:
			if x==i and y==j: continue
			out.append( (x,y) )
	return out

def flash():
	out=0
	for i in range (0, rows):
		for j in range (0, cols):
			if board[i][j]>9:
				for n in getNs(i,j):
					board[n[0]][ n[1]] += 1
				board[i][j]=-9999999999
				out += 1
	return out		


def turn():
	global board
	board = addOne()
	score =0
	while True:
		t = flash()
		score += t
		if t == 0: break
	return score


out =0
for i in range(1,1000000000000):
	out = turn()
	if out == rows * cols:
		print (i)
		break


print(out)



