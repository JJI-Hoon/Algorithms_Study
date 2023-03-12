import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N = int(input())
K = int(input())
K_list = [list(map(int, input().split())) for _ in range(K)]

L = int(input())
L_list = [list(map(str, input().split())) for _ in range(L)]
L_dict = defaultdict(list)
R_dict = defaultdict(list)

graph = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for k in K_list:
    graph[k[0]-1][k[1]-1] = 'K'
for l in L_list:
    if l[1] == 'L':
        L_dict['L'].append(int(l[0]))
    else:
        R_dict['R'].append(int(l[0]))

R_W = [(0,1), (1,0), (0,-1), (-1,0)] 
L_W =[(0,1),(-1,0), (0,-1), (1,0)]

def turn_left(WW, cnt):
    if WW == 'L' or WW == 'X':
        dx = L_W[cnt+1][0]
        dy = L_W[cnt+1][1]
    else:
        if cnt % 2 == 0:
            dx = L_W[cnt+1][0]
            dy = L_W[cnt+1][1]
        else:
            dx = L_W[cnt-1][0]
            dy = L_W[cnt-1][1]
    
    return dx, dy
def turn_right(WW, cnt):
    if WW == 'R' or WW == 'X':
        dx = R_W[cnt+1][0]
        dy = R_W[cnt+1][1]
    else:
        if cnt % 2 == 0:
            dx = R_W[cnt+1][0]
            dy = R_W[cnt+1][1]
        else:
            dx = R_W[cnt-1][0]
            dy = R_W[cnt-1][1]
    
    return dx, dy

def move(x_2, y_2):
    q = deque([[x_2, y_2]])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        X = q.popleft()
        for i in range(4):
            nx = X[0] + dx[i]
            ny = X[1] + dy[i]
            if 0<= nx < N and 0 <= ny < N and visited[nx][ny]:
                return nx, ny
                
cnt = 0
ans = 0
dx, dy = (0, 1)

def dfs(x1, y1, x2, y2, W):
    global dx, dy, cnt, ans
    cnt %= 4

    # 1. 출발
    nx, ny = x1+dx, y1+dy
    if nx < 0 or N <= nx or ny <0 or N <= ny:
        ans = visited[x1][y1]
        return 
    # 2. 방향 전환은 동시에 해주고, 적용은 다음 턴
    if visited[x1][y1] in L_dict['L']:
        dx, dy = turn_left(W, cnt)
        W = 'L'
        cnt += 1 
    elif visited[x1][y1] in R_dict['R']:
        dx, dy = turn_right(W, cnt)
        W = 'R'
        cnt += 1
    
    # 3. 뱀 몸 물면 끝
    if visited[nx][ny]:
        ans = visited[x1][y1]
        return 
    else:
        visited[nx][ny] = visited[x1][y1] + 1

    if graph[nx][ny] != 'K':
        visited[x2][y2] = False
        x2, y2 = move(x2, y2)
        if nx != x2 and ny != y2: 
            visited[x2][y2] = True
        
    dfs(nx, ny, x2, y2, W)

visited[0][0] = True
dfs(0,0,0,0, 'X')
print(ans)