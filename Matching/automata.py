def automata(A, P):
	print(A)
	q = 0
	for i in range(len(A)):
		if q == len(P):
			for _ in range(i-len(P)):
				print(' ', end="") 
			print(P)
			q = 0
		if A[i]==A[q]:
			q += 1


A = "AABAACAADAABAAABAA"
P = "AABA"

automata(A, P)