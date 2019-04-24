#개미 수열

def Anting(a):
	res = ""; a = a + "*"
	c = 0
	for i in range(len(a)-1):
		c += 1
		if a[i] != a[i+1]:
			res += (a[i] + str(c)); c = 0
	return res

a = '1'
for i in range(9):
	print(a)
	a = Anting(a)