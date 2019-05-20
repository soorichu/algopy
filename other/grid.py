def grid(n, s):
	print("grid({0}, {1})".format(n, s), end=" -> ")
	if n==0:
		if s.count('d')==size and s.count('r')==size:
			print(s)
	else:
		for x in ['d', 'r']:
			grid(n-1, s+x)

a = ['d', 'r']
size = 1
grid(size*2, '')