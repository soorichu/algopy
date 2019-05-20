def dupermu2(r, s):
	if r==0:
		print(s)
	else:
		for i in a:
			dupermu2(r-1, s+i)

a = 'HOT'
r = 4
dupermu2(r, '')