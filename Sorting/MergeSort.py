#합병정렬 Merge Sort
#최선과 최악의 평균 수행 시간이 모두 O(n*lon(n))
#안정적 정렬, 비제자리 정렬

import time
import printArr
import strToArr

#시간 재기
start_time = time.time()

#데이터를 입력 받음. space로 구분
#입력 예시 (예1) H E L L O  (예2) 10 23 4 9 012 3
st = input("Input : ")

#입력 받은 string을 array로 바꿈
s = strToArr.strToArr(st)

#합병 정렬(중요)###################################
n = len(s)
MergeSort(s, n):
	if n > 1:
		Mid = int(n/2)
		t[:Mid] = MergeSort(A[:Mid], Mid)
		u[:n-Mid] = MergeSort(A[Mid:n], n-Mid)
		s[:n] = Merge(t[:Mid], s[:n-Mid-1], Mid, n-Mid)
	return s
#################################################
#시간 출력
print("total time :", time.time()-start_time, "millisec")