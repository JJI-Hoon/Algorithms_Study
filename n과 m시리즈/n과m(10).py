n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
s = []

def dfs(depth, N, m, visited):
    global s
    if depth == m:
        print(' '.join(map(str, s)))
        return
    
    remember = 0
    for num in range(len(nums)):
        if not s and not  visited[num] and remember != nums[num]:
            visited[num] = True
            s.append(nums[num])
            remember = nums[num]
            dfs(depth+1, N, m, visited)
            visited[num] = False
            s.pop()
        elif s and not  visited[num] and s[-1] <= nums[num] and remember != nums[num]:
            visited[num] = True
            s.append(nums[num])
            remember = nums[num]
            dfs(depth+1, N, m, visited)
            visited[num] = False
            s.pop()
            
dfs(0, n, m , visited)

# 대소 관계가 아니라, 애초에 깊이가 한 층 깊어질 때 다음 인덱스부터 시작한다면 아... 피라미드처럼 들어가면 되는 구나 0 1 2 순서의 index
# solve(depth+1, i+1, N, M)

N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visited = [False] * N
out = []

def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(idx, N):
        if not visited[i] and overlap != L[i]:
            out.append(L[i])
            visited[i] = True
            overlap = L[i]
            solve(depth+1, i+1, N, M)
            out.pop()
            visited[i] = False

solve(0, 0, N, M)