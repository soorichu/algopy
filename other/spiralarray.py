#배열을 예쁘게 출력하기 위한 함수들
def arrayprint(a, n):
	for i in range(1, n+1):
		for j in range(1, n+1):
			print("%3d" % a[i][j], end = '')
		print('')
	print()

def arrayprintall(a, n):
	for i in range(n+2):
		for j in range(n+2):
			print("%3d" % a[i][j], end = '')
		print('')
	print()


#초기배열 생성
n = 8                 #행열 크기 n*n
di = (0, 1, 0, -1)    #행 방향 스텝
dj = (1, 0, -1, 0)    #열 방향 스텝
a = [[-1]*(n+2) for i in range(n+2)]

for i in range(1, n+1):
	for j in range(1, n+1):
		a[i][j] = 0   #껍데기는 -1이고 안쪽은 0인 (n+2)*(n+2) 배열을 만든다.

arrayprint(a, n)

#스파이럴 생성
i, j, dir = 1, 1, 0

for k in range(1, n*n+1):
	a[i][j] = k
	fi = i+di[dir]    #다음 행 진행방항
	fj = j+dj[dir]    #다음 열 진행방향
	if a[fi][fj]!=0:  #0이 아닌 값을 만나면 
		dir=(dir+1)%4 #행열의 진행방향을 다음 스텝으로 바꾼다. 
	i+=di[dir]
	j+=dj[dir]

arrayprint(a, n)