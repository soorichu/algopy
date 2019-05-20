def partition(n, k, s):
	if n==0:
		print(s[1:])
	for i in range(k, 0, -1):
		if n-i>=0:
			partition(n-i, i, s+'+'+str(i))

n=4
partition(n, n, '')