#선택 정렬 Selection sort
#정렬되지 않은 데이터 중에서 가장 작은 값을 선택하여 미정렬 데이터의 첫 번째 원소와 교환하는 방식
#총비교횟수 n(n-1)/2, 시간복잡도 O(n^2)
#제자리 정렬, 안정적이지 않은 정렬

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

#선택정렬(중요)###################################
for i in range(len(s)-1):
	Min = i #일단 미정렬 데이터의 첫번째 원소를 기준(최소)으로 지정
	for j in range(i+1, len(s)): #그 다음 원소들 중 최솟값을 찾는다.
		if s[Min] > s[j]:  #기준 원소보다 작은 원소를 찾은 경우
			Min = j; #그 원소가 가장 작은 원소가 된다.
	#이렇게 한 스텝이 지나면 i번째 원소 뒤의 원소 중 가장 작은 것이 몇 번째(Min)인지 알게 된다.
	#이제 Min 번째 원소와 (맨앞) i번째 원소를 바꾸면 된다.
	s[i], s[Min] = s[Min], s[i]
	printArr(s, i+1)  #정렬된 배열 출력
#################################################
#시간 출력
print("total time :", time.time()-start_time, "millisec")