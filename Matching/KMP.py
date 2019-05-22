#KMP 알고리즘(Knuth, Morris, Pratt) --> 인터넷에서 퍼온 것
#KMP 알고리즘은 매칭 과정에서 불일치가 일어났을 때 처음부터 다시 비교하지 않고 
#중간부터 비교할 수 있도록 되돌아갈 위치를 배열로 나타낸 것이다. 
#오토마타에서는 문자 각가에 대해 돌아갈 곳을 명사히지만 KMP에서는 문자별로 구별하지 않아 전처리 시간이 줄어든다.
#수행시간은 O(n)

class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]
        
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
        
    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in S
        """
        partial, ret, j = self.partial(P), [], 0
        
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                ret.append(i - (j - 1))
                j = 0
            
        return ret
        

if __name__=="__main__":
	A = "AABAACAADAABAAABAA"
	P = "AABA"
	kmp = KMP().search(A, P)
	print(A)
	for i in kmp:
		print("{0}{1}".format(" "*i, P))