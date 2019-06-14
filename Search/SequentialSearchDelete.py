from SequentialSearch import SequentialSearch

def SequentialSearchDelete(A, n, x):
	index = SequentialSearch(A, n, x)
	if(index==-1):return A, n
	A[Index] = A[n-1]
	return A, n-1