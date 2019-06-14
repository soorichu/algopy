def SequentialSearchInsert(A, n, x):
	A.append(x)# A[n] = x
	return A, n+1

if __name__=="__main__":
	A = [6, 2, 7, 1, 9, 3, 5, 4]
	print(SequentialSearchInsert(A, len(A), 0))