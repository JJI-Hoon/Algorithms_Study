import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
ans = []
cnt = 0

def dfs(s, cnt):
    global G
    if G-S % U-D != 0 or G-S // U-D < 0:
        return
    
    if s == G:
       ans.append(cnt) 
       return
   
    if s > G:
        dfs(s-D, cnt + 1)
    elif s < G:
       dfs(s+U, cnt + 1)
    return

dfs(S, 0)   
print(min(ans) if ans else "use the stairs")

# DFS 문제점 종료조건이 까다로움, 반례가 많음

# BFS는 큐가 없어지면 종료인데, 종료조건이 까다로운건 BFS 먼저 떠올리기

import sys
from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        if v == G:
            return count[G]
        for i in (v+U, v-D):
            if 0 < i <= F and not visited[i]:
                visited[i] = True
                count[i] = count[v] + 1
                q.append(i)
    if count[G] == 0:
        return "use the stairs"
    
input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
visited = [0 for i in range(F+1)]
count = [0 for i in range(F+1)]
print(bfs(S))
        