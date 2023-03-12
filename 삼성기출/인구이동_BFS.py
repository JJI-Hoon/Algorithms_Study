import sys
from collections import deque
input = sys.stdin.readline


N, L, R = map(int, input().split())
Maps = [list(map(int, input().split())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
#  국경선 여는 동시에 값을 저장

def bfs(x, y):
    global people, flag
    Q = deque()
    print(Q)
    Q.append([x, y])
    temp = [[x, y]]
    while Q:
        x, y = Q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(Maps[x][y] - Maps[nx][ny]) <= R:
                visited[nx][ny] = True
                Q.append([nx, ny])
                print(Q)
                temp.append([nx, ny])
    
    return temp
        
ans = 0
    
while True:
    visited = [[False] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                temp = bfs(i, j)
                # 이렇게하면 visited[i][j] = True 사용가능
                if len(temp) > 1:
                    flag = True
                    number  = sum([Maps[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        Maps[x][y] = number

    if not flag:
        break
    
    ans += 1
    
print(ans)
