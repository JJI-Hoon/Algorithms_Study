import sys
input = sys.stdin.readline

def dfs(x, y):
    if graph[x][y] == '-' and y+1 < m and graph[x][y+1] == '-':
        dfs(x, y+1)
    elif graph[x][y] == '|' and x+1 < n and graph[x+1][y] == '|':
        dfs(x+1, y)
    graph[x][y] = '.'
    return 1

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] != '.':
            ans += dfs(i, j)

print(ans)   
