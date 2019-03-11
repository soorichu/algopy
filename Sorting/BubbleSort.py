# 버블정렬 Bubble Sort
#모든 인접한 두 값을 비교하여 왼쪽 값이 더 큰 경우에는 자리를 바꾸는 방법을 반복해서 정렬하는 방식
#총비교횟수는 n(n-1)/2, 시간복잡도는 O(n^2)
#안정적 정렬, 제자리 정렬

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

#버블정렬(중요)###################################
for i in range(len(s)-1):
	exchange = False  
	for j in range(len(s)-1-i):
		if s[j] > s[j+1]:  #왼쪽이 큰 경우
			s[j], s[j+1] = s[j+1], s[j] #두 원소의 자리를 바꾼다.
			exchange = True
	#이렇게 한 스텝이 끝나면 가장 큰 원소가 맨 뒤로 가게 되므로
	#그 다음 번에는 그 원소를 제외한 앞의 원소들만 비교하면 된다.
	if exchange==False : break;  #(개선)바뀐게 하나도 없다면 종료시킨다.
	printArr(s, i+1)  #정렬된 배열 출력
#################################################

