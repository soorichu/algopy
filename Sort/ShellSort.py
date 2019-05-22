#쉘 정렬 Shell Sort
#삽입 정렬은 삽입될 위치를 찾기 위해 한 번에 한 자리씩만 이동하기 떄문에 제자리를 찾아가는데 느리다.
#    -> 이 단점을 보완한 것이 Shell 정렬
#성능 O(n*log(n)) ~ O(n^2)
#간격의 크기 D를 계산하는 방식에 따라 성능이 달라진다. D의 가장 좋은 간격은 미해결 과제
#불안정 정렬, 제자리 정렬

from InsertSort import InsertSort

def MakeSub(A, f, l, t):
	res = []
	for i in range(f, l, t):
		res.append(A[i])
	return res

def ShellSort(A, n):
	D = int(n/2)
	print(A)
	while D > 0:
		for i in range(0, D):
			val = i
			for s in InsertSort(MakeSub(A, i, n, D), int(n/D)):
				A[val] = s; val+=D

		D = int(D/2)


if __name__=="__main__":
	A = [6, 2, 7, 1, 9, 3, 5, 4]
	ShellSort(A, len(A))