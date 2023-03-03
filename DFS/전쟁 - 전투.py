import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(m)]
W_cnt = 0
B_cnt = 0

def dfs(x, y, country):
    global W_cnt, B_cnt
    if country == 'W':
        W_cnt += 1
    elif country == 'B':
        B_cnt += 1
    
    graph[x][y] = '.'
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == country:
            dfs(nx, ny, country)

W_list = []
B_list = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W':
            dfs(i, j, graph[i][j])
            W_list.append(W_cnt**2)
            W_cnt = 0
        elif graph[i][j] == 'B':
            dfs(i, j, graph[i][j])
            B_list.append(B_cnt**2)
            B_cnt = 0
            
print(sum(W_list), sum(B_list))

