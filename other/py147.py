#숫자 검사

def check(arr):
	return len(arr) == len(set(arr))

a = '6789301245'
print(check(a))

b = '012322456789'
print(check(b))