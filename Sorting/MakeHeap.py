#힙정렬
#완전이진트리 최대힙

import math

s = [60, 20, 70, 10, 80, 30, 50, 40]
n = len(s)

print("Input :", s)
for i in range(n):
	par = math.ceil(i/2)-1
	print("par : s[{0}] = {1}, i : s[{2}] = {3}".format(par, s[par], i, s[i]))
	while(par>=0 and s[par]<s[i]):
		print("s[{0}]={1} <-> s[{2}]={3}".format(par, s[par], i, s[i]))
		s[par], s[i] = s[i], s[par]
		i = par
		par = math.ceil(i/2)-1
		print(s)


#궁금증 : 힙정렬에서 어차피 오름차순으로 정리할텐데 
#        왜 처음 힙을 만들 떄 작은 것을 부모노드 쪽으로 놓지 않고
#        거꾸로 큰것을 부모노드로 놓아 만드는 것일까?
#        처음 힙을 만들 떄 작은~큰 순으로 하면 나중에 정렬 시 더 시간을 절약할 수 있을 것 같은데...