from sys import stdin
import heapq

INF = int(1e9)
dists, res = [], []

def dijkstra(start: int, n: int) -> None:
    global dists, res
    
    hq = []
    for i in range(1, n + 1):
        if i == start:
            continue
        heapq.heappush(hq, (dists[start][i], i))
    
    while hq:
        now_dist, now_vertex = heapq.heappop(hq)
        
        if dists[start][now_vertex] < now_dist:
            continue
        for next_vertex in range(1, n + 1):
            # 자기 자신으로 가는 경로는 제외
            if now_vertex == next_vertex or start == next_vertex:
                continue
            # node를 우회할 때 start에서 neighbor 까지의 최단거리가 되는 경우
            if now_dist + dists[now_vertex][next_vertex] < dists[start][next_vertex]:
                dists[start][next_vertex] = now_dist + dists[now_vertex][next_vertex]
                heapq.heappush(hq, (now_dist + dists[now_vertex][next_vertex], next_vertex))
                # node로 가는 첫 번째 집하장을 neighbor 경로에 저장
                res[start][next_vertex] = res[start][now_vertex]
    
def main():
    def input():
        return stdin.readline().rstrip()
    
    global dists, res
    
    n, m = map(int, input().split())
    dists = list(([INF] * (n + 1)) for _ in range(n+1))
    res = [['-'] * (n + 1) for _ in range(n + 1)]
    
    for _ in range(m):
        a, b, w = map(int, input().split())
        dists[a][b] = dists[b][a] = w
        res[a][b] = str(b)
        res[b][a] = str(a)
    
    for i in range(1, n + 1):
        dijkstra(i, n)
    
    for line in res[1:]:
        print(*line[1:], sep = ' ')
        
if __name__ == "__main__":
    main()