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
def Merge(A, p, q, r):
	i = q-1; j = q; t = 0; temp = [range(len(A))]
	count = 0
	while i < q and j < r:
		if A[i] < A[j]:
			temp[t] = A[i]; t+=1; i+=1;
		else: 
			temp[t] = A[j]; t+=1; j+=1;
	
	while i < q:
		temp[t] = A[i]; t+=1; i+=1;
	
	while j < r:
		temp[t] = A[j]; t+=1; j+=1;

	i = p-1; t = 0;
	while i < r:
		A[i] = temp[t]; t+=1; i+=1;

	count += 1
	printArr.printArr(A, count)

def MergeSort(A, p, r):
	if p < r:
		q = int((p+r)/2)
		MergeSort(A, p, q)
		MergeSort(A, q+1, r)
		Merge(A, p, q, r)
#################################################

MergeSort(s, 0, len(s))

#시간 출력
print("total time :", time.time()-start_time, "millisec")

