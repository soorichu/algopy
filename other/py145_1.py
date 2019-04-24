#특별한 정렬

s = [-1, 1, 3, -2, 2]

sm = []; sp = []
for si in s:
	if si < 0: sm.append(si)
	else: sp.append(si)

for s in sm: print(s, end=" ")
for s in sp: print(s, end=" ")
