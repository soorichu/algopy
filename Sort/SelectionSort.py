#선택 정렬 Selection sort
#정렬되지 않은 데이터 중에서 가장 작은 값을 선택하여 미정렬 데이터의 첫 번째 원소와 교환하는 방식
#총비교횟수 n(n-1)/2, 시간복잡도 O(n^2)
#불안정 정렬, 제자리 정렬


def SelectionSort(A, n):
	count = 0
	print(A)
	for last in range(n-1, 0, -1):
		Max = last  # 가장 마지막 원소를 최댓값으로 설정함.
		print("{0}{1}".format(" "*(3*Max+1), A[Max]))
		for k in range(last):
			if A[k] > A[Max]:  
				Max = k  # 앞의 미정렬 원소 중에서 최댓값을 구함.
		A[Max], A[last] = A[last], A[Max]  # 최댓값을 뒤로 보내 정렬함.
		print("{0}{1}".format(" "*(3*Max+1), A[Max])) 
		print(A)
		count += 1
	return A

A = [6, 2, 7, 1, 9, 3, 5, 4]
print(SelectionSort(A, len(A)))