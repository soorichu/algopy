#쉘 정렬 Shell Sort
#삽입 정렬은 삽입될 위치를 찾기 위해 한 번에 한 자리씩만 이동하기 떄문에 제자리를 찾아가는데 느리다.
#    -> 이 단점을 보완한 것이 Shell 정렬
#성능 O(n*log(n)) ~ O(n^2)
#간격의 크기 D를 계산하는 방식에 따라 성능이 달라진다. D의 가장 좋은 간격은 미해결 과제
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

#쉘 정렬(중요)###################################
def MakeSub(s, first, last, term):
	res = []
	for i in range(first, last, term):
		res.append(s[i])
	return res

count = 0
D = int(len(s)/2)
while D > 0:
	for i in range(0, D):
		sub = MakeSub(s, i, len(s), D) #부분배열 만들기
		for j in range(1, len(sub)):  #부분배열을 삽입정렬
			for k in range(j, 0, -1):
				if sub[k-1] > sub[k]:
					s[(k-1)*D+i], s[k*D+i] = s[k*D+i], s[(k-1)*D+i]
					count += 1
					printArr(s, count)
				else: break
	D = int(D/2)
#################################################
#시간 출력
print("total time :", time.time()-start_time, "millisec")