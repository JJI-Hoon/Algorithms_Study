from collections import deque
import copy
# (0,1) -> (-1,0) -> (0, -1) -> (1, 0)

n = int(input())

idx = ((0,1), (-1,0), (0,-1), (1,0))
direction = {0: (0,1)
             , 1: (-1, 0)
             , 2: (0, -1)
             , 3: (1, 0)}

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
visited = [[False] * 100 for _ in range(100)]

def bfs(x, y, dir, N):
    q = deque([])
    tmp = deque([dir])
    for _ in range(N+1):
        while tmp:
            d = tmp.popleft()
            D = idx[d]
            if 0 <= x+D[0] < 100 and 0 <= y + D[1] < 100:
                visited[x+D[0]][y+D[1]] = True
                x, y = x+D[0], y + D[1]
            q.append((d+1)%4)
        tmp = copy.deepcopy(q)

def check(x, y):
    for i in range(3):
        x, y = x+idx[i][0], y+idx[i][1]
        if 0 > x or x >= 100 or 0 > y or y >= 100 or not visited[x][y]:
            return 0
    return 1
        
for i in range(n):
    x, y, d, g = map(int, input().split())
    dd = idx.index(direction[d])
    visited[x][y] = True
    print(dd)
    bfs(x, y, dd, g)

ans = 0
for i in range(100):
    for j in range(100):
        if visited[i][j]:
            ans += check(i, j)

print(ans)
