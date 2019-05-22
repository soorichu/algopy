#원시 매칭 알고리즘
#원시적인 알고리즘은 텍스트의 각 위치에서 시작해 패턴 문자열과 일치하는지 체크하는 방법
#수행시간은 O(mn)

def naiveMatching(A, P):
	print(A)
	n = len(A); m = len(P)
	for i in range(n-m+1):
		if P == A[i:i+m]:
			for _ in range(i):
				print(' ', end="") 
			print(P)

if __name__=="__main__":
	A = "AABAACAADAABAAABAA"
	P = "AABA"

	naiveMatching(A, P)