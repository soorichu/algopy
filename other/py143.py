text = "aaaaaaabbcccdeeeeffffffg"
res = ""
c = 0
first = True
for i in range(len(text)-1):
	if first: res += text[i]; first = False
	c += 1
	if text[i]!=text[i+1]: 
		res += str(c); first = True; c = 0

print(res)