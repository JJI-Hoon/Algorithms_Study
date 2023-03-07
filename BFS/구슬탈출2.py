import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()

# 초기화 함수
def init():
    rx, ry, bx, by = [0] * 4
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

# 이동 함수
def move(x, y, dx, dy):
    count = 0 # 이동한 칸 수
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

# 그래프 탐색 함수 BFS
def bfs():
    init()
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            break
        for i in range(len(dx)):
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i])
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i])
            
            if board[next_bx][next_by] == 'O':
                continue
            if board[next_rx][next_ry] == 'O':
                print(depth)
                return
            if next_rx == next_bx and next_ry == next_by:
                if r_count > b_count:
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]
                    
            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx, next_ry, next_bx, next_by, depth+1))
    print(-1)
    
bfs()