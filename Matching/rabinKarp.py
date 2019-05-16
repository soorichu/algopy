def list2int(arr):
	res = 0; n = len(arr)
	for i in range(n):
		res += ord(arr[i])*n**i
	return res

def rabinKarp(A, P, d):
	print(A)
	n=len(A); m=len(P)
	p = list2int(P)
	for i in range(n-m):
		if p == list2int(A[i:i+m]):  #다시 구현
			for _ in range(i):
				print(' ', end="") 
			print(P)


A = "AABAACAADAABAAABAA"
P = "AABA"

rabinKarp(A, P, len(P))