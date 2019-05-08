n = 4
a = [[0]*(n+1) for i in range(n+1)]

for i in range(1, n+1):
	for j in range(1, n+1):
		a[i][j] = (n+1-i)*n -j+1 if i%4 == j%4 or (i%4+j%4)==1 else (i-1)*n+j

for i in range(1, n+1):
	for j in range(1, n+1):
		print("%4d" %a[i][j], end="")
	print('\n')
