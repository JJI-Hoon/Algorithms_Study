import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

def dfs(S):
    global cnt
    visited[S] = cnt
    
    for i in graph[S]:
        if not visited[i]:
            cnt += 1
            dfs(i)
    return

dfs(start)
print(graph)
for i in range(1, n+1):
    print(visited[i])
    
# Graph의 크기를 node만큼 늘려주지 않음
# why? 정점(Node)이 1부터 시작함을 인지 X
# graph의 노드 별로 연결 노드를 표현하는 방법 -> 인접 리스트  
# [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []] -> 1번 노드에 2, 4 위의 간선의 개수만큼 for문 돌려주면 효율적 코드 짤 수 있음