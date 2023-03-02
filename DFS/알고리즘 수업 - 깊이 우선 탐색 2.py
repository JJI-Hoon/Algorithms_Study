'''
dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 내림차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for road in roads:
    a, b = road[0], road[1]
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort(reverse = True)


def dfs(x):
    global cnt
    visited[x] = cnt
    
    for N in graph[x]:
        if not visited[N]:
            cnt += 1
            dfs(N)
    return

dfs(r)

for i in visited[1:]:
    print(i)