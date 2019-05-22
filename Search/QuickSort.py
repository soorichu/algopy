# 퀵정렬
#피벗을 기준으로 주어진 배열을 두 부분 배열로 분할하고
#각 부분 배열에 대해서 퀵 정렬을 순환적으로 적용하는 방식.

def Partition(A, n):
	Left = 1; Right = n-1;

	while Left < Right:
		#Left는 pivot보다 큰 값을 찾는다.
		while Left<n and A[Left]<A[0]: Left += 1
		#Right는 pivot보다 작은 값을 찾는다.
		while Right>0 and A[Right]>=A[0]: Right -= 1
		if Left < Right: 
			A[Left], A[Right] = A[Right], A[Left]
			print("Left<->Right", A)
		else:
			A[0], A[Right] = A[Right], A[0]
			print("pivot<->Right", A)

	return Right

def QuickSort(A, n):
	if n > 1:
		pivot = Partition(A, n)
		print("pivot", pivot)
		A[:pivot] = QuickSort(A[:pivot], pivot)
		A[pivot+1:] = QuickSort(A[pivot+1:], n-pivot-1)
		print("Quicking", A)
	return A

if __name__=="__main__":
	A = [30, 45, 20, 15, 40, 25, 35, 10]
	A = QuickSort(A, len(A))
	print(A)