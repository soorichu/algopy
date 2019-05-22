def KMP(A, P):
	pi = []
	pi = preprocessing(P)
	i=0; j=0; m=len(P); n=len(A)
	while(i<n):
		if j==0 or A[i]==P[j]:
			i+=1; j+=1
		else:
			j = pi[j]
		if j==m+1:
			print(A[i-m])
			j = pi[j]

def preprocessing(P):
	j = 0; m=len(P)
	k = -1; pi = [0]*(m+1)
	while j<=m:
		if k==0 or P[j]==P[k]:
			j+=1; k+=1;
			pi[j]=k
		else:
			k = pi[k]
	return pi


A = "AABAACAADAABAAABAA"
P = "AABA"
KMP(A, P)