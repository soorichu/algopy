#쉘 정렬 Shell Sort
#삽입 정렬은 삽입될 위치를 찾기 위해 한 번에 한 자리씩만 이동하기 떄문에 제자리를 찾아가는데 느리다.
#    -> 이 단점을 보완한 것이 Shell 정렬
#성능 O(n*log(n)) ~ O(n^2)
#간격의 크기 D를 계산하는 방식에 따라 성능이 달라진다. D의 가장 좋은 간격은 미해결 과제
#불안정 정렬, 제자리 정렬


def MakeSub(s, first, last, term):
	res = []
	for i in range(first, last, term):
		res.append(s[i])
	return res

count = 0
A = [6, 2, 7, 1, 9, 3, 5, 4]
D = int(len(A)/2)
while D > 0:
	for i in range(0, D):
		sub = MakeSub(A, i, len(A), D) #부분배열 만들기
		for j in range(1, len(sub)):  #부분배열을 삽입정렬
			for k in range(j, 0, -1):
				if sub[k-1] > sub[k]:
					A[(k-1)*D+i], A[k*D+i] = A[k*D+i], A[(k-1)*D+i]
					count += 1
					print(A)
				else: break
	D = int(D/2)
