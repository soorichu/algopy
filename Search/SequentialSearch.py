def SequentialSearch(A, n, x):
	for i in range(n):
		if A[i] is x: return i
	return -1

if __name__=="__main__":
	A = [6, 2, 7, 1, 9, 3, 5, 4]
	print(SequentialSearch(A, len(A), 3))