#삽입 정렬 Insert Sort
#주어진 데이터를 하나씩 뽑은 후, 나열된 데이터들이 항상 정렬된 형태를 가지도록 뽑은 데이터를 바른 위치에 삽입해서 나열하는 방식
#미정렬 부분에서 첫번째 데이터를 정렬 부분에서 제자리를 찾아 삽입함.
#역순으로 정렬된 경우 O(n^2), 순서대로 정렬된 경우 O(n)
#삽입 정렬은 데이터의 입력되는 상태에 따라 수행시간이 달라진다.
#입력이 거의 정렬된 경우 어떤 알고리즘보다 빠른 수행시간을 가짐. 
#안정적인 정렬, 제자리 정렬

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

#삽입정렬(중요)###################################
def InsertSort(A, n):
	count = 0
	for i in range(1, n):
		loc = i-1;  newItem = A[i];
		while loc>=0 and newItem < A[loc]:
			A[loc+1] = A[loc]
			loc -= 1
		A[loc+1] = newItem
		count += 1
		printArr.printArr(A, count)

#################################################

InsertSort(s, len(s))  # 실행

#시간 출력
print("total time :", time.time()-start_time, "millisec")