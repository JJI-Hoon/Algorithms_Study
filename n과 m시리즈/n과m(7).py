n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []

def dfs():
    global s, nums
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for num in nums:
        if not s:
            s.append(num)
            dfs()
            s.pop()
        elif s and s[-1] <= num:
            s.append(num)
            dfs()
            s.pop()
        
    return

dfs()