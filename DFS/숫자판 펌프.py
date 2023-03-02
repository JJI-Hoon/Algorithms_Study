# 하나의 좌표에 대해서 DFS 실행하면서 전 좌표 반복문 실행

import sys
input = sys.stdin.readline

graph = [list(map(str, input().split())) for _ in range(5)]

def dfs(x, y, number):
    if len(number) == 6:
        result.add(number)
        return
        
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, number + graph[nx][ny])
            
result = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])

print(len(result))