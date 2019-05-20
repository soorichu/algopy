# perm(['1', '2', '3'], []) -> perm(['2', '3'], ['1']) -> perm(['3'], ['1', '2']) -> perm([], ['1', '2', '3']) -> 123
#                                                         perm(['2'], ['1', '3']) -> perm([], ['1', '3', '2']) -> 132
#                              perm(['1', '3'], ['2']) -> perm(['3'], ['2', '1']) -> perm([], ['2', '1', '3']) -> 213
#                                                         perm(['1'], ['2', '3']) -> perm([], ['2', '3', '1']) -> 231
#                              perm(['1', '2'], ['3']) -> perm(['2'], ['3', '1']) -> perm([], ['3', '1', '2']) -> 312
#                                                         perm(['1'], ['3', '2']) -> perm([], ['3', '2', '1']) -> 321

def perm(a, b):
	print("perm({0}, {1})".format(a, b), end=" -> ")
	if not len(a):
		print(''.join(b))
	for i in range(len(a)):
		b.append(a.pop(i))
		perm(a, b)
		a.insert(i, b.pop())

n = 3
p = [str(i) for i in range(1, n+1)]
perm(p, [])