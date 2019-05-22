#힙 정렬(Heap Sort)
#힙 정렬은 힙이라는 특수한 자료구조를 사용하는 정렬 알고리즘이다.(최소/최대힙 이용)
#힙은 이진 트리로서 맨 아래 층을 제외하고는 완전히 채워져 있고 맨 아래층은 왼쪽부터 꽉 채워져 있다.
#힙의 모든 노드는 하나씩의 값을 가지고 있는데 다음 힙의 성질을 만족한다.
# "각 노드의 값은 자기 자식의 값보다 작다."
#힙정렬은 주어진 배열을 힙으로 만든 후 힙에서 가장 작은 값을 차례로 하나씩 제거하면서 힙의 크기를 줄여 나간다. 
#나중에 힙에 아무런 원소도 남지 않으면 힙 정렬이 끝난다. 
#시간복잡도는 O(nlogn)이다. 
#불안정적 정렬, 제자리 정렬

#초기 최대힙 생성
def BuildHeap(A, n):
	print("초기힙 생성")
	for i in range(n):
		temp = i
		print(i, A[:i+1], end="->")
		par = int((i+1)/2)-1 #부모노드
		while(par>=0 and A[par]<A[i]): #부등호 바꾸면 최대힙
			A[par], A[i] = A[i], A[par]
			i = par  #부모의 부모와도 힙 만들기
			par = int((i+1)/2)-1
		print(A[:temp+1])
	return A

def HeapSort(A, n):
	print(A)
	A = BuildHeap(A, n)
	print(A)
	print("힙 정렬")
	for i in range(n-1, 0, -1):
		A[0], A[i] = A[i], A[0]  #불안정적
		print(i, A[:i+1], end="->")
		p = 0; l = 1; r = 2
		while l<i:
			if r<i and A[r]>A[l]: l = r
			if A[l]>A[p]: 
				A[p], A[l] = A[l], A[p]
			print(A[:l+1], end="->")
			p = l; l = 2*p+1; r = 2*p+2

		print(A)

	return A


A = [6, 2, 7, 1, 9, 3, 5, 4]
print(HeapSort(A, len(A)))
