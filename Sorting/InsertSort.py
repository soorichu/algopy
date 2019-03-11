#삽입 정렬 Insert Sort
#주어진 데이터를 하나씩 뽑은 후, 나열된 데이터들이 항상 정렬된 형태를 가지도록 뽑은 데이터를 바른 위치에 삽입해서 나열하는 방식
#미정렬 부분에서 첫번째 데이터를 정렬 부분에서 제자리를 찾아 삽입함.


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
for i in range(1, len(s)): #0번째 항은 정렬된 원소로 두고 1번째 원소부터 시작
	pick = s[i]  #미정렬 부분 중 첫번쨰 원소를 뽑는다.
	for j in range(i, 0, -1):  
		if s[j] < s[j-1]:  
			s[j], s[j-1] = s[j-1], s[j]
		else: break
		
	printArr(s, i+1)  #정렬된 배열 출력
#################################################