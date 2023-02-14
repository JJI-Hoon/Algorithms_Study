import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [[] for _ in range(r)]
remember = dict()

for i in range(r):
    graph[i].extend(list(input().strip()))
    for j in graph[i]:
        remember[j] = 0
        
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0

def dfs(x, y, cnt):
    global ans, remember
    ans = max(ans, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <=ny < c and remember[graph[nx][ny]] == 0:
                remember[graph[nx][ny]]  = 1
                dfs(nx, ny, cnt+1)
                remember[graph[nx][ny]] = 0
    return ans

remember[graph[0][0]] = 1
print(dfs(0, 0, 1))