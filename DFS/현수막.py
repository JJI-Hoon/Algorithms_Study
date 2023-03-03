import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
graph = [list(input().split()) for _ in range(m)]
ans = 0

def dfs(x, y):
    dx = [0, 0, 1, -1, 1, -1, 1, -1]
    dy = [1, -1, 0, 0, -1, 1, 1, -1]
    graph[x][y] = '0'
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == '1':
            dfs(nx, ny)
            
for i in range(m):
    for j in range(n):
        if graph[i][j] == '1':
            dfs(i, j)
            ans += 1

print(ans)