import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
check = [list(map(int, input().split())) for _ in range(k)]
for c in check:
    graph[c[0]-1][c[1]-1] = 1

size = 0
ans = 0

def dfs(x, y):
    global size
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            size += 1
            # 방문 처리
            graph[nx][ny] = 0
            dfs(nx, ny)
            
    return 
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dfs(i, j)
            # 구역 별로 크기 구하고, 새 구역의 크기는 Size Reset시키면서 다시 스타트 
            ans = max(size, ans)    
            size = 0
            
print(ans)

