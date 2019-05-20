def grid2(n, s):
	if n==0:
		if s.count('d')==size and s.count('r')==size:
			print(s)
	else:
		for x in 'dr':
			grid2(n-1, s+x)

size = 2
grid2(size*2, '')