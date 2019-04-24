#8의 개수

count = 0
for i in range(10000):
	count += str(i).count('8')

print(count)