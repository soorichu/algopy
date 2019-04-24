# 퀵정렬
#피벗을 기준으로 주어진 배열을 두 부분 배열로 분할하고
#각 부분 배열에 대해서 퀵 정렬을 순환적으로 적용하는 방식.

def Partition(A, n):
	Left = 1; Right = n-1;
	#Left는 pivot보다 큰 값을 찾는다.
	while Left<n and A[Left]<A[0]: Left += 1
	#Right는 pivot보다 작은 값을 찾는다.
	while Right>0 and A[Right]>=A[0]: Right -= 1
	if Left < Right: 
		A[Left], A[Right] = A[Right], A[Left]
	else:
		A[0], A[Right] = A[Right], A[0]

	return Right

def QuickSort(A, n):
	if n > 1:
		print(0, A, end="=>")
		pivot = Partition(A, n)
		print(1, A)
		QuickSort(A[:pivot], pivot)
		print(2, A)
		QuickSort(A[pivot+1:], n-pivot-1)
		print(3, A)
		

A = [30, 45, 20, 15, 40, 25, 35, 10]
QuickSort(A, len(A))