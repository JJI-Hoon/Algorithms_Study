import sys
from collections import deque
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
visited_ = [[False] * M for _ in range(N)]
ans = 0

error1 = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            error1 += 1
            
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    Q = deque()
    Q.append([x, y])
    visited_[x][y] = True
    
    while Q:
        x, y = Q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph_[nx][ny] == 0 and not visited_[nx][ny]:
                Q.append([nx, ny])
                visited_[nx][ny] = True
                
    return 
    
def check():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph_[i][j] == 2 and not visited_[i][j]:
                bfs(i, j)
    
    error2 = 0
    for i in range(N):
        error2 += sum(visited_[i])
    # print(cnt)
    return N*M - (error2 + error1 + 3)

def dfs(cnt):
    global ans, graph_, visited_
    # print(visited)
    if cnt == 3:
        tmp = check()
        ans = max(tmp, ans)
        visited_ = [[False] * M for _ in range(N)]
        return
    
    for x in range(N):
        for y in range(M):
            if 0 <= x < N and 0 <= y < M and not visited[x][y] and graph_[x][y] != 2 and graph_[x][y] != 1:
                visited[x][y] = True
                graph_[x][y] = 1
                dfs(cnt + 1)
                graph_[x][y] = 0
                visited[x][y] = False
    
    return

graph_ = copy.deepcopy(graph)
visited = [[False] * M for _ in range(N)]
dfs(0)

print(ans)