#삽입 정렬 Insert Sort
#주어진 데이터를 하나씩 뽑은 후, 나열된 데이터들이 항상 정렬된 형태를 가지도록 뽑은 데이터를 바른 위치에 삽입해서 나열하는 방식
#미정렬 부분에서 첫번째 데이터를 정렬 부분에서 제자리를 찾아 삽입함.
#역순으로 정렬된 경우 O(n^2), 순서대로 정렬된 경우 O(n)
#삽입 정렬은 데이터의 입력되는 상태에 따라 수행시간이 달라진다.
#입력이 거의 정렬된 경우 어떤 알고리즘보다 빠른 수행시간을 가짐. 
#시간복잡도 O(n^2)
#안정적인 정렬, 제자리 정렬

def InsertSort(A, n):
	print(A)
	for i in range(1, n):
		loc = i-1;  newItem = A[i];
		while loc>=0 and newItem < A[loc]:
			A[loc+1] = A[loc]
			print("{0}{1}".format(" "*(3*loc+4), newItem))
			loc -= 1
		if A[loc+1]!=newItem:
			A[loc+1] = newItem
		print(A)
	return A

if __name__=="__main__":
	A = [6, 2, 7, 1, 9, 3, 5, 4]
	print(InsertSort(A, len(A)))
