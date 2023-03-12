import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = []

def dfs(x, y, cnt, Value):
    global ans
    if cnt == 4:
        ans.append(Value)
        return
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1, Value + graph[nx][ny])
            visited[nx][ny] = False
    
    return

def mid_check(x, y):
    global ans
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # 4가지 방향인데, 방향 만드려면 3번의 반복이 필요함
    # 이걸 이렇게 표현하네
    for a in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = graph[x][y]
        for b in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (a+b)%4
            nx = x+dx[t]
            ny = y+dy[t]

            if not (0 <= nx < n and 0 <= ny < m):
                tmp = 0
                break
            tmp += graph[nx][ny]
        # 최대값 계산
        ans.append(tmp)
        
    return


for i in range(n):
    for j in range(m):
        # Mistake 1 : Visited 처음 방문 표시
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = False
        
        mid_check(i, j)
        
print(max(ans))
    

###########################################################################################################################################################################################
# 2차원 배열에서 최대 값 찾는 코드    
# max(map(max, arr))

# 또 다른 풀이
import sys; input = sys.stdin.readline

def dfs(r, c, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc])
                visit[nr][nc] = 0



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0

print(ans)

########################################################################################################################################