s = [1, 3, 4, 8, 13, 17, 20]
pairs = list(zip(s[0:], s[1:]))
pairs.sort(key=lambda x:x[1]-x[0])
print(pairs[0])