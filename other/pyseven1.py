# 각 수에 대한 코드값 구하기
d0 = ' - '
d1 = '  |'
d2 = '| |'
d3 = '|  '
d4 = '   '
d = [d0, d1, d2, d3, d4]

D0 = [' - ', '| |', '   ', '| |', ' - ']
#  - 
# | |
#
# | |
#  -
D1 = ['   ', '  |', '   ', '  |', '   ']
#
#   |
#
#   |
#
D2 = [' - ', '  |', ' - ', '|  ', ' - ']
#  -
#   |
#  - 
# |
#  - 
D3 = [' - ', '  |', ' - ', '  |', ' - ']
 # -
 #  |
 # - 
 #  |
 # -
D4 = ['   ', '| |', ' - ', '  |', '   ']
#
# | |
#  -
#   |
#
D5 = [' - ', '|  ', ' - ', '  |', ' - ']
#  -
# |
#  -
#   |
#  -
D6 = [' - ', '|  ', ' - ', '| |', ' - ']
#  -
# |
#  -
# | |
#  -
D7 = [' - ', '  |', '   ', '  |', '   ']
 # -
 #  |
#
 #  |
#
D8 = [' - ', '| |', ' - ', '| |', ' - ']
#  -
# | |
#  -
# | |
#  -
D9 = [' - ', '| |', ' - ', '  |', ' - ']
#  -
# | |
#  -
#   |
#  -

D = [D0, D1, D2, D3, D4, D5, D6, D7, D8, D9]

for i in range(10):
  temp = ''
  print(i, D[i], end=" => ")
  for dd in D[i]:
    if dd == d0: temp += '0'
    if dd == d1: temp += '1'
    if dd == d2: temp += '2'
    if dd == d3: temp += '3'
    if dd == d4: temp += '4'
  D[i] = temp
  print(D[i])

#문제 풀기
n = 617676435413576
row, col = 3, 4
print("\n==> 입력 값 : {0}, 가로 {1}, 세로 {2}".format(n, 3, 4))
for i in range(5):
  res = ''
  for x in str(n):
    #print(d[int(D[int(x)][i])], end="")
    temp = d[int(D[int(x)][i])]
    temp = temp[0]+temp[1]*col+temp[2]
    res += temp
  print(res)
  if i % 2 == 1: 
    for r in range(row-1): 
      print(res)
  