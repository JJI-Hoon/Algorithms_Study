# 파이썬 sys recursion limit 크게 하니까 메모리 초과나네
# recursion늘리면 메모리 늘어남
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
# map(lambda x: str(x), A)
graph = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(r)]
remember = [0] * 26
        
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 1

def dfs(x, y, cnt):
    global ans, remember
    ans = max(ans, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <=ny < c and remember[graph[nx][ny]] == 0:
                remember[graph[nx][ny]]  = 1
                dfs(nx, ny, cnt+1)
                remember[graph[nx][ny]] = 0
    return ans

remember[graph[0][0]] = 1
print(dfs(0, 0, 1))