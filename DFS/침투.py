# import sys
# input = sys.stdin.readline

# m, n = map(int, input().split())
# graph = [list(input().strip()) for _ in range(m)]
# ans = []

# def dfs(x, y):
#     if x == m-1:
#         ans.append('YES')
#         return 
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#     graph[x][y] = '1'
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == '0':
#             dfs(nx, ny)
            
# for i in range(n):
#     if graph[0][i] == '0':
#         dfs(0, i)
#     if 'YES' in ans:
#         break

# print('YES' if 'YES' in ans else 'NO')

a = 1
b = [1,2,3, 4]
if 1 in b or 2 in b or 3 in b or 4 in b or 5 in b or 6 in b:
    print(1)