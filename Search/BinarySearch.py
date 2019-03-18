# 이진 탐색
#1. 입력이 정렬된 리스트에 대해서만 적용이 가능하다.
#2. 데이터의 사빕/삭제 연산을 수행하면 데이터의 이동이 발생
#데이터 삽입/삭제 후에는 데이터를 정렬 상태로 유지하기 위해 평균적으로 n/2개의 데이터를 
#이동해야 하기 때문에 삽입과 삭제가 빈번한 응용에서의 탐색으로 적합하지 않음. 

import math

#순환형태로 짠 경우
def BinarySearch(A, Left, Right, x):
	if Left > Right : return -1

	Mid = math.floor((Left+Right)/2)

	if x == A[Mid]: return Mid
	elif x < A[Mid]: BinarySearch(A, Left, Mid-1, x)
	else: BinarySearch(A, Mid+1, Right, x)

#반복형태로 짠 경우
def BinarySearchIteration(A, n, x):
	Left = 0
	Right = n-1
	while(Left <= Right):
		Mid = math.floor((Left+Right)/2)
		if x == A[Mid]: return Mid
		elif x < A[Mid]: Right = Mid - 1
		else: Left = Mid + 1

	return -1

A = [i*10 for i in range(10)]
print(BinarySearch(A, 0, len(A)-1, 40))
print(BinarySearchIteration(A, len(A), 40))