#라빈-카프 알고리즘
#문자열의 비교를 수치의 비교로 전환해 문자열을 매칭하는 방법
#수행시간 O(n)

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

if __name__=="__main__":
	A = "AABAACAADAABAAABAA"
	P = "AABA"
	rabinKarp(A, P, len(P))