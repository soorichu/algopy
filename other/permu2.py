def perm2(r, s):
	if r==0:
		t = True
		for i in range(1, n+1):
			if s.count(str(i))!=1: 
				t = False; break
		if t: print(s)
	else:
		for i in range(1, n+1):
			perm2(r-1, s+str(i))

n = 3
perm2(n, '')
