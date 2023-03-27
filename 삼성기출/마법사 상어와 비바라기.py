# 파이썬은 기본적으로 내림을 하고(5/2를 float로 2.0) 양수 나머지만 허용합니다. 그래서 -7=3*-3 + 2
import copy
import sys

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
direction = [(0,0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0,1), (1, 1), (1, 0), (1, -1)]
xy_list = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]

def move(xy_list, dir, s):
    tmp = []
    for X in xy_list:
        X_ = (X[0] + dir[0] * cnt) % N
        Y_ = (X[1] + dir[1] * cnt) % N
        graph[X_][Y_] += 1
        tmp.append((X_ , Y_))
    
    return tmp
            
def first_change(xy_list):
    for T in xy_list:
        x, y = T[0], T[1]
        for idx in range(2, 9, 2):
            X, Y = x + direction[idx][0], y + direction[idx][1]
            if 0 <= X < N and 0 <= Y < N and graph[X][Y] >= 1:
                print(x, y, X, Y)
                graph[x][y] += 1
    return 

for _ in range(M):
    d, s = map(int, input().split())
    dir, cnt = direction[d], s % N
    xy_list = move(xy_list, dir,cnt)
    print(xy_list)
    first_change(xy_list)
    # print(graph)
    tmp = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and (i, j) not in xy_list:
                tmp.append((i, j))
                graph[i][j] -= 2
    # print(graph)
    print()
    print(tmp)
    xy_list = copy.deepcopy(tmp)
    
ans = sum(sum(t) for t in graph)
print(ans)
# print(graph)
