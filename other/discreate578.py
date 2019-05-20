import numpy as np
def Insert(A, n):
	for i in range(1, n):
		print("***key={0}***".format(i))
		j = i-1
		while j >= 0:
			if A[j] > A[j+1]: 
				A[j], A[j+1] = A[j+1], A[j]
			print(A)
			j -= 1

A = np.random.choice(20, 10)
print(A)
Insert(A, len(A))