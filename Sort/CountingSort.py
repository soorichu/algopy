#계수정렬
import time
import printArr
import strToArr

#데이터를 입력 받음. space로 구분
#입력 예시 (예1) H E L L O  (예2) 10 23 4 9 012 3
st = input("Input : ")

#시간 재기
start_time = time.time()

#입력 받은 string을 array로 바꿈
s = strToArr.strToArr(st)

def CountingSort(A, n):
	oldA = A[0]
	if type(oldA) == type('a'):	
		A = [ord(a) for a in A]
	Min = Max = A[0]

	for i in range(n):
		if A[i]<Min: Min = A[i]
		if A[i]>Max: Max = A[i]

	count = [0 for i in range(Max+1)]

	for i in A: count[i] += 1
		
	# 출현 횟수 누적값 계산
	for i in range(Min+1, Max+1): 
		count[i] = count[i]+count[i-1]

	B = [0 for i in range(n)]
	for i in range(n-1, -1, -1):
		B[count[A[i]]-1] = A[i]
		count[A[i]] -= 1

	if type(B[0])!=type(oldA): B = [chr(b) for b in B]
	return B

printArr.printArr(CountingSort(s, len(s)))
#시간 출력
print("total time :", time.time()-start_time, "millisec")

