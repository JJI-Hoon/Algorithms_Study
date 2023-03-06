import sys
import heapq 
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)

for i in range(M):
    a, b, cow = map(int, input().split())
    graph[a].append((cow, b))
    graph[b].append((cow, a))

def dijkstra(S):    
    Q = []
    distance = [INF] * (N+1)
    
    heapq.heappush(Q, (0, S))
    distance[S] = 0
    
    while Q:
        now_dist, now_vertex = heapq.heappop(Q)
        
        if now_dist > distance[now_vertex]:
            continue
        
        for next_dist, next_vertex in graph[now_vertex]:
            if now_dist + next_dist < distance[next_vertex]:
                distance[next_vertex] = now_dist + next_dist
                heapq.heappush(Q, (now_dist + next_dist, next_vertex))
    
    return distance

print(dijkstra(1)[N])