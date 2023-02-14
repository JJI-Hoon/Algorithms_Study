n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for num in numbers:
        if num not in s:
            s.append(num)
            dfs()
            s.pop()

    return

dfs()