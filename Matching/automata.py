#오토마타 매칭 --> 인터넷에서 퍼온 것
#매칭 과정에서 불일치가 일어났을 때 처음부터 다시 비교하지 않고 
#문백상의 정보(상태전이함수)를 이용해 중간부터 비교할 수 있도록 한 것이다.
#수행시간은 O(n+|Σ|m), O(|Σ'|m+|Σ|) 

MAX = 256
  
def getNextState(P, M, state, x): 
    if state < M and x == ord(P[state]): 
        return state+1
    i=0
    for ns in range(state,0,-1): 
        if ord(P[ns-1]) == x: 
            while(i<ns-1): 
                if P[i] != P[state-ns+1+i]: 
                    break
                i+=1
            if i == ns-1: 
                return ns  
    return 0
  
def computeTF(P, M): 
    global MAX 
  
    TF = [[0 for i in range(MAX)] for _ in range(M+1)] 
  
    for state in range(M+1): 
        for x in range(MAX): 
            z = getNextState(P, M, state, x) 
            TF[state][x] = z 
  
    return TF 
  
def search(P, A): 
    global MAX 
    M = len(P) 
    N = len(A) 
    TF = computeTF(P, M)     
  
    # Process A over FA. 
    state=0
    for i in range(N): 
        state = TF[state][ord(A[i])] 
        if state == M: 
            print("{0}{1}".format(" "*(i-M+1), P))
            
  
if __name__=="__main__":
    A = "AABAACAADAABAAABAA"
    P = "AABA"
    print(A)
    search(P, A) 
