#계수 정렬(Counting Sort)
#비교 기반의 정렬이 아닌 값의 분포를 이용하여 정렬하는 방식
#계수 정렬은 입력 원소의 값이 어떤 작은 정수 범위 내에 있다는 것을 알고 있는 경우에 적용할 수 있는 방법으로,
#주어진 원소 중에서 자신보다 작거나 같은 값을 갖는 원소의 개수를 개산하여 정렬할 위치를 찾음.

def CountingSort(A, n):
	Min = Max = A[0]

	for i in range(n):
		if A[i]<Min: Min = A[i]
		if A[i]>Max: Max = A[i]

	count = [0]*(Max+1)

	for i in A: count[i] += 1
	print(A, "출현횟수", count)
	# 출현 횟수 누적값 계산
	for i in range(Min+1, Max+1): 
		count[i] = count[i]+count[i-1]
	print(A, "누적  값", count)

	B = [0 for i in range(n)]
	for i in range(n-1, -1, -1):
		B[count[A[i]]-1] = A[i]
		count[A[i]] -= 1

	return B

A = [7, 5, 9, 8, 4, 5, 7, 5]
print(CountingSort(A, len(A)))

