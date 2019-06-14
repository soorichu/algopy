import math

def BinarySearch(A, Left, Right, x):
	if Left > Right : return -1

	Mid = int(math.floor((Left+Right)/2))

	if x == A[Mid]: return Mid
	elif x < A[Mid]: BinarySearch(A, Left, Mid-1, x)
	else: BinarySearch(A, Mid+1, Right, x)

def BinarySearchIteration(A, n, x):
	Left = 0
	Right = n-1
	while(Left <= Right):
		Mid = int(math.floor((Left+Right)/2))
		if x == A[Mid]: return Mid
		elif x < A[Mid]: Right = Mid - 1
		else: Left = Mid + 1

	return -1
	
if __name__=="__main__":
	A = [i*10 for i in range(10)]
	print(BinarySearch(A, 0, len(A)-1, 40))
	print(BinarySearchIteration(A, len(A), 40))