def strToArr(st):
	s = st.split(" ")   # 데이터를 배열로 만듦
	i = 0
	while i < len(s):
		if s[i]=="": del s[i]  # 공백 원소 삭제
		else:
			if s[i].isdecimal() : s[i] = int(s[i]) #숫자인 경우 int로 바꾸어 넣어 주기
			i += 1
	return s