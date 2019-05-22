def automata3(P, A):
	m = len(P)
	n = len(A)
	q = 0
	for i in range(len(set(A))):
		for q in range(m):
			if q == 3:
				print("s[{0}][{1}]={2}".format(q, i, sg[q][i]))


A = "AABAACAADAABAAABAA"
P = "AABA"
sg = [[1, 0, 0, 0], 
      [2, 2, 0, 0],
      [1, 0, 0, 0],
      [1, 4, 0, 0],
      [5, 0, 0, 0]]

automata3(P, A)