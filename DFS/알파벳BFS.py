import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(r)]
remember = [0] * 26
remember[graph[0][0]] = 1
q = deque([[0, 0]])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 1

while q:
    cnt += 1
    print(q)
    print(cnt)
    x, y = q.pop()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <=ny < c and not remember[graph[nx][ny]]:
            q.append([nx, ny])
            remember[graph[nx][ny]] = cnt

print(remember)
print(max(remember))

## BFS

### BFS set
## 문자열안에 문자가 있는 파악하면 되는 군
import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 1
def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])
    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)

BFS(0, 0)
print(answer)