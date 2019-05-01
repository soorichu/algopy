#1차원 라이프 게임

def life(a, n):
	size = len(a)
	for _ in range(n):
		a = a[-1]+a+a[0]
		s = ''
		for i in range(1, size+1):
			s += str((int(a[i-1])+int(a[i])+int(a[i+1]))%2)
		a = s
	return a

print(life('10101000101111', 5))