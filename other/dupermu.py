def dupermu(r, s):
	if r==0:
		print(s)
	else:
		for i in range(1, n+1):
			dupermu(r-1, s+str(i))

n, r = 3, 4
dupermu(r, '')
