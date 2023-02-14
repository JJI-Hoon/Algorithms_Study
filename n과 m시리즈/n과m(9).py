# n, m = map(int, input().split())
# nums = sorted(list(map(int, input().split())))

# output = []
# visited = [False] * n
# check = []

# def dfs(visited,check):
#     global output
#     if sum(visited) == m:
#         print(output, check, visited)
#         if output not in check:
#             check.append(output)
#             print(' '.join(map(str, output)))
#             return
#         else:
#             return
#     for i in range(len(nums)):
#         print(f'count : {i}', check)
#         if not visited[i]:
#             print(i, i, i)
#             output.append(nums[i])
#             visited[i] = True
#             # print(visited)
#             dfs(visited, check)
#             print(output, check)
#             output.pop()
#             visited[i] = False
#     return
# dfs(visited, check)

# remember_me 변수를 통해서 중복이 되는 것을 방지할 수 있음

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(n):
        if not visited[i] and remember_me != nums[i]:
            visited[i] = True
            temp.append(nums[i])
            remember_me = nums[i]
            dfs()
            visited[i] = False
            temp.pop()

dfs()