#순위 정하기

def rank(arr):
	arr2 = arr[:]
	arr2.sort()
	for a in arr:
		print("%2d : %d" %(a, arr2.index(a)))


s = [55, 33, 0, 77, 4, 33, 77, 88, 77, 99]
rank(s)