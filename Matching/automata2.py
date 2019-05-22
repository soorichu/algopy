MAX = 256
  
def getNextState(pat, M, state, x): 
    if state < M and x == ord(pat[state]): 
        return state+1
    i=0
    for ns in range(state,0,-1): 
        if ord(pat[ns-1]) == x: 
            while(i<ns-1): 
                if pat[i] != pat[state-ns+1+i]: 
                    break
                i+=1
            if i == ns-1: 
                return ns  
    return 0
  
def computeTF(pat, M): 
    global MAX 
  
    TF = [[0 for i in range(MAX)] for _ in range(M+1)] 
  
    for state in range(M+1): 
        for x in range(MAX): 
            z = getNextState(pat, M, state, x) 
            TF[state][x] = z 
  
    return TF 
  
def search(pat, txt): 
    global MAX 
    M = len(pat) 
    N = len(txt) 
    TF = computeTF(pat, M)     
  
    # Process txt over FA. 
    state=0
    for i in range(N): 
        state = TF[state][ord(txt[i])] 
        if state == M: 
            print("Pattern found at index: {}".format(i-M+1)) 
  
        
txt = "AABAACAADAABAAABAA"
pat = "AABA"
search(pat, txt) 
