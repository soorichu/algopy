from random import randint

def checkAll(a):
	for ay in a:
		for axy in ay:
			if axy == 0: return True
	return False

def printAll(a):
	for ay in a:
		for axy in ay:
			print("%3d" % axy, end= " ")
		print()

xsize, ysize = 8, 6
x, y = 4, 3
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

a = [[0]*xsize for _ in range(ysize)]
a[y][x] = 1  #초기 위치
step = 1

while checkAll(a):
	k = randint(0, 7)
	(tx, ty) = (x+dx[k], y+dy[k])
	if (0<=tx<xsize) and (0<=ty<ysize):
		a[ty][tx] += 1
		step += 1
	print(checkAll(a))


printAll(a)
print('steps:', step)