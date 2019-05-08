fin = open('input.txt')
fout = open('output.txt', 'w')

#------방향 데이터 받기---------------
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

# (1, -1) (0, 1) (1, 1)
# (0, -1)   ME   (0, 1)
# (-1,-1) (-1,0) (-1,1)

d = list(zip(di, dj))
print(d)

#------input 데이터------------------
mine = []
for f in fin.readlines():
	mine.append(list(f))

print(mine)
m, n = len(mine), len(mine[0])

#------지뢰찾기----------------------
result = []
for i in range(m):
	line = ''
	for j in range(n):
		if mine[i][j]=='*':
			line+='* '
		else:
			s=0
			for k in range(8):
				ti, tj = i+d[k][0], j+d[k][1]
				if 0<=ti<m and 0<=tj<n:
					if mine[ti][tj]=='*':
						s += 1
			line+=str(s)+' '
	result.append(line+'\n')

#-----결과출력-----------------------
for i in result:
	fout.write(i)

fin.close()
fout.close()
