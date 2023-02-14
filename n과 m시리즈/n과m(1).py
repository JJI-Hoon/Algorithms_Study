n,m = list(map(int,input().split()))
 
s = []

# n과 m - 2
def check(S):
    for i in range(len(S)-1):
        if S[i] > S[i+1]:
            return False
    return True
        
# n과 m - 1
def dfs():
    global s
    if len(s)==m and check(s):
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
 
dfs()