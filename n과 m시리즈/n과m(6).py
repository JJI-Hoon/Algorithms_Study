n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for num in numbers:
        if not  s:
            s.append(num)
            dfs()
            s.pop()
        elif s and s[-1] < num:
            s.append(num)
            dfs()
            s.pop()

    return

dfs()

##############################################################################

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    for i in range(start, n):
        if nums[i] not in temp:
            temp.append(nums[i])
            dfs(i + 1)
            temp.pop()
dfs(0)