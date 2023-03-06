import sys
import heapq

'''
* 3개의 Array 필요
graph : distance, Node
distance : INF 설정
q(list) : heapq에 사용될 리스트
'''

input = sys.stdin.readline
N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]

for i in range(D):
    graph[i].append((1, i+1))
    

for i in range(N):
    start, end, length = map(int, input().split())
    if end > D:
        continue
    graph[start].append((length, end))

# 초기 각 노드마다 거리 Setting
INF = 10 ** 8
distance = [INF] * (D+1)
distance[0] = 0

q = []
heapq.heappush(q, (0, 0))
while q:
    d, now = heapq.heappop(q)
    if distance[now] < d:
        continue
    
    for x in graph[now]:
        cost = d + x[0]
        
        if distance[x[1]] > cost:
            distance[x[1]] = cost
            heapq.heappush(q, (cost, x[1]))

print(distance[D])
            