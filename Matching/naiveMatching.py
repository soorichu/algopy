def naiveMatching(A, P):
	print(A)
	n = len(A); m = len(P)
	for i in range(n-m+1):
		if P == A[i:i+m]:
			for _ in range(i):
				print(' ', end="") 
			print(P)

A = "AABAACAADAABAAABAA"
P = "AABA"

naiveMatching(A, P)