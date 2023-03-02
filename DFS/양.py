import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global v, o
    if graph[x][y] == 'v':
        v += 1
    elif graph[x][y] == 'o':
        o += 1
    graph[x][y] = '#'
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#':
            dfs(nx, ny)
                
r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
V, O, v, o = 0, 0, 0, 0

for i in range(r):
    for j in range(c):
        if graph[i][j] != '#':
            dfs(i, j)
            if o > v:
                v = 0
            else:
                o = 0
            V += v
            O += o
            v, o = 0, 0

print(O, V)