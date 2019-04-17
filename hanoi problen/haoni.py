def Hanoi(n, fr, to, ext):
	if n==1:
		print(n, fr, "->", to)
	else:
		Hanoi(n-1, fr, ext, to)
		print(n, fr, "->", to)
		Hanoi(n-1, ext, to, fr)

Hanoi(5, "A", "C", "B")