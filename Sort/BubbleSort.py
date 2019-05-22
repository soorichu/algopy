# 버블정렬 Bubble Sort
#모든 인접한 두 값을 비교하여 왼쪽 값이 더 큰 경우에는 자리를 바꾸는 방법을 반복해서 정렬하는 방식
#총비교횟수는 n(n-1)/2, 시간복잡도는 O(n^2)
#안정적 정렬, 제자리 정렬


def BubbleSort(A, n):
	print(A)
	count = 0; flag = True;
	for last in range(n-1, 0, -1):
		for i in range(0, last):
			if A[i] > A[i+1]:
				A[i], A[i+1] = A[i+1], A[i]
				print("{0}{1}  {2}".format(" "*(3*i+1), A[i], A[i+1]))
				flag = False
		if flag: break
		count += 1
	return A 

#################################################

A = [6, 2, 7, 1, 9, 3, 5, 4]
print(BubbleSort(A, len(A)))


