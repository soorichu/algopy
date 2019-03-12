#삽입 정렬 Insert Sort
#주어진 데이터를 하나씩 뽑은 후, 나열된 데이터들이 항상 정렬된 형태를 가지도록 뽑은 데이터를 바른 위치에 삽입해서 나열하는 방식
#미정렬 부분에서 첫번째 데이터를 정렬 부분에서 제자리를 찾아 삽입함.
#역순으로 정렬된 경우 O(n^2), 순서대로 정렬된 경우 O(n)
#삽입 정렬은 데이터의 입력되는 상태에 따라 수행시간이 달라진다.
#입력이 거의 정렬된 경우 어떤 알고리즘보다 빠른 수행시간을 가짐. 
#안정적인 정렬, 제자리 정렬

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

#삽입정렬(중요)###################################
for i in range(1, len(s)): # i 이상은 미정렬 데이터(0은 정렬데이터 취급)
	for j in range(i, 0, -1): # i 미만의 정렬 데이터
		if s[j] < s[j-1]:  #(j(미정렬처음), j-1(정렬끝)), .... , (1, 0) 이렇게 비교
			s[j], s[j-1] = s[j-1], s[j]
		else: break #제자리를 찾으면 시간 낭비하지 않고 break
		
	printArr(s, i+1)  #정렬된 배열 출력
#################################################
#시간 출력
print("total time :", time.time()-start_time, "millisec")