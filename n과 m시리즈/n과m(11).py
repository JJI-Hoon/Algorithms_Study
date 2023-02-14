n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s = []

def dfs(depth, N, M):
    if depth == M:
        print(' '.join(map(str, s)))
        return
    
    remember = 0
    for i in range(n):
        if remember != nums[i]:
            s.append(nums[i])
            remember = nums[i]
            dfs(depth+1, N, M)
            s.pop()

    return

dfs(0, n, m)