#합병정렬 Merge Sort
#최선과 최악의 평균 수행 시간이 모두 O(n*lon(n))
#안정적 정렬, 비제자리 정렬

#시간 재기
import time
start_time = time.time()
#데이터를 입력 받음. space로 구분
#입력 예시 (예1) H E L L O  (예2) 10 23 4 9 012 3
st = input("Input : ")
s = st.split(" ")   # 데이터를 배열로 만듦
i = 0
while i < len(s):
	if s[i]=="": del s[i]  # 공백 원소 삭제
	else:
		if s[i].isdecimal() : s[i] = int(s[i]) #숫자인 경우 int로 바꾸어 넣어 주기
		i += 1

#출력하기 함수 만들어 놓기
def printArr(s, n):
	print("Step{0} :".format(n), end=" " )
	for i in s:
		print(i, end=" ")
	print()

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