import sys
input = sys.stdin.readline


N, L, R = map(int, input().split())
Maps = [list(map(int, input().split())) for _ in range(N)]
people = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]


#  국경선 여는 동시에 값을 저장
def dfs(x, y):
    global people, flag
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(Maps[x][y] - Maps[nx][ny]) <= R:
            flag = True
            people.extend([[x, y], [nx, ny]])
            visited[x][y] = True
            visited[nx][ny] = True
            dfs(nx, ny)
            
    return 

def change_map(i, j, p, flag):
    global dd
    if p:
        n = 0
        c = 0
        dd += 1
        for i in range(N):
            for j in range(N):
                if visited[i][j] and not check[i][j]:
                    check[i][j] = dd
                    n += Maps[i][j]
                    c += 1

        person = n // c
        for i in range(N):
            for j in range(N):
                if check[i][j] == dd:
                    Maps[i][j] = person
                    
    return
        
ans = 0
    
while True:
    visited = [[False] * N for _ in range(N)]
    check = [[False] * N for _ in range(N)]
    dd = 0
    flag = False
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                people = []
                dfs(i, j)
                change_map(i, j, people, flag)
  
    if not flag:
        break
    
    ans += 1
    
print(ans)

# DFS로 풀 시 -> 80%에서 시간초과 남
# Why? DFS의 시간복잡도 공부 필요
# 시간복잡도로 인해서 BFS로 풀어야 되는 경우 생각하기
