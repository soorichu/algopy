from random import randint

def walk(ysize, xsize, y, x):
	def isall():
		r = False
		for y in range(ysize):
			for x in range(xsize):
				if a[y][x]==0:
					r = True
			return r

	a = [[0]*xsize for i in range(ysize)]
	a[y][x] = 1
	step = 1
	while isall():
		k = randint(0, 7)
		tx, ty = x+dx[k], y+dy[k]
		if(0<=tx<xsize) and (0<=ty<ysize):
			x, y = tx, ty
			a[y][x] += 1
			step += 1
	for y in range(ysize):
		for x in range(xsize):
			print("%3d" % a[y][x], end='')
		print('')
	print('steps:', step)


dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
walk(8, 6, 4, 3)