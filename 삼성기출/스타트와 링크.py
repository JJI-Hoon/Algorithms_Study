def dfs(depth, idx):
    global min_diff
    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                # 2. 이와 같이 첫 번째 팀 구성
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                # 3. 나머지 팀 구성 (어짜피 절반으로 구성되도록 정했기 때문에)
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return
    # 1. 팀 경우의 수 파악 : idx 하나씩 늘려가면서, 0 -> 1~N -> 2~N
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


n = int(input())

visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0)
print(min_diff)