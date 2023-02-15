'''
DFS & DP 알고리즘 활용

* 틀린 이유
1. DFS로 테케는 맞췄으나, 시간복잡도 측면에서 시간초과가 남
why? 500 * 500 에서 상하좌우 4가지 방향을 한 블럭마다 다 해주면 시간초과가 2초인 문제에서
당연히 에러가 발생함 ,, 이 부분을 깊게 생각하지 않음 (문제를 오랜만에 풀어서 그런듯)

2. 시간 복잡도를 낮추려면 ? 불필요한 연산 수를 줄여야 함 ,,
How? 전체 문제의 최적해가 부분 문제의 최적해로 쪼개질 수 있도록 해야 함 (블럭으로 생각하면 이해 OK)
이 부분은 블로그에 따로 정리
'''
######################################################################
# 나의 풀이 Only DFS

import sys
input = sys.stdin.readline

m, n = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(m)]
ans = 0

dx = [0, 0, 1]
dy = [1, -1, 0]


def dfs(x, y):
    global ans
    if x == m-1 and y == n-1:
        ans += 1
        return
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0<= ny < n and map[x][y] > map[nx][ny]:
            dfs(nx, ny)

dfs(0, 0)
print(ans)

#######################################################################

# 정답 DFS X DP
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def dfs(sx, sy):
    # 도착 지점에 도달하면 1(한 가지 경우의 수)를 리턴
    if sx == m-1 and sy == n-1:
        return 1

    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if dp[sx][sy] != -1:
        return dp[sx][sy]
    
    ways = 0
    for i in range(4):
        nx, ny = sx + dx[i], sy + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[sx][sy] > graph[nx][ny]:
            ways += dfs(nx, ny)
    
    dp[sx][sy] = ways
    return dp[sx][sy]


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx, dy = [1,-1,0,0], [0,0,1,-1]
print(dfs(0,0))
print(dp)