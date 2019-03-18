
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

sp = type(s[0]) == type('a')
#s = [7, 5, 9, 8, 4, 5, 7, 5]
if sp: 
	sl = s 
#	print("sl", sl)
	s = [ord(st) for st in s]

n = len(s)
Min = Max = s[0]

for i in range(n):
	if s[i]<Min: Min = s[i]
	if s[i]>Max: Max = s[i]

count = [0 for i in range(Max+1)]

for i in s: count[i] += 1
	
#print(count)
# 출현 횟수 누적값 계산
for i in range(Min+1, Max+1): 
	count[i] = count[i]+count[i-1]

#print(count)

r = [0 for i in range(n)]
for i in range(n-1, -1, -1):
	r[count[s[i]]-1] = s[i]
	count[s[i]] -= 1

if sp: r = [chr(rt) for rt in r]

printArr.printArr(r)