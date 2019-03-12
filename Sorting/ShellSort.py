#쉘 정렬 Shell Sort
#삽입 정렬은 삽입될 위치를 찾기 위해 한 번에 한 자리씩만 이동하기 떄문에 제자리를 찾아가는데 느리다.
#    -> 이 단점을 보완한 것이 Shell 정렬

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