#배열 바꾸기

a = ['a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5']
b = []

for i in range(int(len(a)/2)): 
	temp = int(len(a)/2) + i
	b.append(a[i]); b.append(a[temp])

print(b)