#https://m.blog.naver.com/askmrkwon/220768685076


n = 4
a = [[0]*(n+1) for i in range(n+1)]

for i in range(1, n+1):
	for j in range(1, n+1):
		print("%3d%d" %(i, j), end=" ")
	print()
print()


count = 1                              #count = n*(i-1)+j
for i in range(1, n+1):
	for j in range(1, n+1):
		if i%4==j%4 or (i%4+j%4)%4==1: #i==j or i+j==n+1
			a[i][j] = n*n-count+1
		else:
			a[i][j] = count
		count+=1


#출력
for i in range(1, n+1):
	for j in range(1, n+1):
		print("%4d" % a[i][j], end=" ")
	print()

print("\n가로합", end=" : ")
for i in range(1, n+1):
	print("%d" %sum(a[i][:]), end=" ")

print("\n세로합", end=" : ")
for i in range(1, n+1):
	print("%d" %sum(a[:][j]), end=" ")

sum1, sum2 = 0, 0
for i in range(1, n+1):
	sum1 += a[i][i]
	sum2 += a[i][n+1-i]
print("\n사선합 : %d %d"% (sum1, sum2))
