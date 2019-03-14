#선택 정렬 Selection sort
#정렬되지 않은 데이터 중에서 가장 작은 값을 선택하여 미정렬 데이터의 첫 번째 원소와 교환하는 방식
#총비교횟수 n(n-1)/2, 시간복잡도 O(n^2)
#불안정 정렬, 제자리 정렬

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

#선택정렬(중요)###################################
def SelectionSort(A, n):
	count = 0
	for last in range(n-1, 0, -1):
		Max = last  # 가장 마지막 원소를 최댓값으로 설정함.
		for k in range(last):
			if A[k] > A[Max]:  
				Max = k  # 앞의 미정렬 원소 중에서 최댓값을 구함.
		A[Max], A[last] = A[last], A[Max]  # 최댓값을 뒤로 보내 정렬함. 
		count += 1
		printArr.printArr(A, count)
#################################################

SelectionSort(s, len(s))  # 실행

#시간 출력
print("total time :", time.time()-start_time, "millisec")