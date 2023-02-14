n, m = map(int, input().split())
s = []

def dfs():
    global s
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n+1):
        if not s:
            s.append(i)
            dfs()
            s.pop()
        elif s and s[-1] <= i:
            s.append(i)
            dfs()
            s.pop()
    
    return

dfs()