import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 나의 풀이
def dfs(x, y):
    global visited
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny]:
            graph[nx][ny] += graph[x][y]
            dfs(nx, ny)
            graph[x][y] = graph[nx][ny]
            
    return graph[x][y]

####################################################################################

# 다른 사람 풀이
# 1. graph[x][y] = 0 으로 visited 처리 가능해짐, graph조건 자체도가능해지구나
# 2. cnt 변수를 하나만 늘려감으로써, 개수 카운트해주고 (어짜피 1인애들만 count가 되니까)
# 3. 내 코드보다 이게 더 간결하고 가독성이 좋은 듯
def dfs(x,y):
    global cnt
    cnt += 1
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<n and -1<ny<m and graph[nx][ny]==1:
            dfs(nx,ny)

####################################################################################

# 나의 코드
cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:
            cnt += 1
            ans = max(dfs(i, j), ans)

if not cnt:
    print(0)
    print(0)
else:
    print(cnt)
    print(ans)

####################################################################################

# 다른사람 코드
num_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt=0
            dfs(i,j)
            num_list.append(cnt)

if len(num_list)==0:
    print(len(num_list))