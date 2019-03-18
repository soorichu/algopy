# 버블정렬 Bubble Sort
#모든 인접한 두 값을 비교하여 왼쪽 값이 더 큰 경우에는 자리를 바꾸는 방법을 반복해서 정렬하는 방식
#총비교횟수는 n(n-1)/2, 시간복잡도는 O(n^2)
#안정적 정렬, 제자리 정렬

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

#버블정렬(중요)###################################
def BubbleSort(A, n):
	count = 0; flag = True;
	for last in range(n-1, 0, -1):
		for i in range(0, last):
			if A[i] > A[i+1]:
				A[i], A[i+1] = A[i+1], A[i]
				flag = False
		if flag: break
		count += 1
		printArr.printArr(A, count)

#################################################

BubbleSort(s, len(s))  # 실행
#시간 출력
print("total time :", time.time()-start_time, "millisec")

