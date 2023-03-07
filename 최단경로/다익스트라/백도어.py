import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
Cant_see = list(map(int, input().split()))
graph = [[] for _ in range(N)]
INF = int(1e18)

for i in range(M):
    A, B, dist = map(int, input().split())
    graph[A].append((dist, B))
    graph[B].append((dist, A))

def dijkstra(S):
    Q = []
    heapq.heappush(Q, (0, S))
    distance = [INF] * N
    distance[S] = 0
    
    while Q:
        now_dist, now_vertex = heapq.heappop(Q)
        if now_dist > distance[now_vertex]:
            continue
        
        for next_dist, next_vertex in graph[now_vertex]:
            if now_dist + next_dist < distance[next_vertex] and not Cant_see[next_vertex]:
                distance[next_vertex] = now_dist + next_dist
                heapq.heappush(Q, (now_dist + next_dist, next_vertex))
            elif now_dist + next_dist < distance[next_vertex] and next_vertex == N-1:
                distance[next_vertex] = now_dist + next_dist
                heapq.heappush(Q, (now_dist + next_dist, next_vertex))
                
    return distance

distance = dijkstra(0)
print(distance[N-1] if distance[N-1] != INF else -1)   
    