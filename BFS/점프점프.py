import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A_list = list(map(int, input().split()))
visited= [False] * N

def bfs(S):
    Q = deque([S])
    visited[S] = 0
    
    while Q:
        s = Q.popleft()
        if s == N-1:
            print(visited)
            return visited[N-1]
        
        for i in range(1, A_list[s]+1):
            if s+i < N and not visited[s+i]:
                Q.append(s+i)
                visited[s+i] = True
                visited[s+i] = visited[s] + 1

    if not visited[N-1]:
        return -1

print(bfs(0))